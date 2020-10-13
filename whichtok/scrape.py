# module with code to scrape data from TikTok
import pandas as pd
from TikTokApi import TikTokApi
import json

api = TikTokApi()



class user_group:
    """hold information about a group of users"""
    users_dict = {} # a dictionary of user information (keys are usernames)
    user_likes = {}

    def __str__(self):
        return str(self.users_dict)

    def load_from_json(self, json_stream):
        self.users_dict = json.load(json_stream)

    def __init__(self, seed_user=None, group_size=None, json_out=None, json_in=None):
        """load user group from dictionary or corresponding json"""
        if seed_user != None and group_size != None:
            json_out_stream = open(json_out, 'w')
            suggested_n = crawl_user_set(seed_user, group_size, user_data_output=json_out_stream)
            json_out_stream.close()

            user_group_dict = {}
            for username in suggested_n:
                user_dict = suggested_n[username]
                likes, sugg_hashtags, sugg_sounds, videos = fetch_user_info(user_dict, n_likes=10, n_videos=10, n_sugg_hashtags=10, n_sugg_sounds=10)
                user_group_dict[username] = {}
                user_group_dict[username]['likes'] = likes
                user_group_dict[username]['sugg_hashtags'] = sugg_hashtags
                user_group_dict[username]['sugg_sounds'] = sugg_sounds
                user_group_dict[username]['videos'] = videos
                
            self.users_dict = user_group_dict

        elif json_in:
            self.users_dict = load_from_json(json_in)

        else:
            raise 'Error: plase specify `json` or `seed_user` and `group_size`'
        
    def make_user_graph(self):
        """form a graph"""
        pass
    def make_video_graph(self):
        """form a graph"""
        pass


def crawl_user_set(seed_username, n, user_data_output=None):
    """
    Get a list of tiktok users from the given username.

    Keyword arguments:
    seed_username -- the user to use as a seed
    n -- number of users to fetch
    user_data_output -- optional output stream to write user information to as JSON
    """
    seed_id = api.getUser(seed_username)['userInfo']['user']['id']
    suggested_n = api.getSuggestedUsersbyIDCrawler(count=n, startingId=seed_id)
    suggested_n = user_list_to_dict(suggested_n)

    if user_data_output:
        json.dump(suggested_n, user_data_output, indent='\t')

    return suggested_n
    
    # alternatively: suggested_n = pd.DataFrame(suggested_n).drop(['extraInfo','keyToken','playToken'], axis=1)

def clean_user_dict(user_info_dict):
    username = user_info_dict['subTitle'][1:]
    return_dict = {}

    for info_field in ['title','id','description','link']:
        return_dict[info_field] = user_info_dict[info_field]
    for info_field in ['verified','fans','likes','secUid','relation']:
        return_dict[info_field] = user_info_dict['extraInfo'][info_field]
    return_dict['username'] = username

    return return_dict

def user_list_to_dict(user_info_dicts):
    """load a list of tiktok user info dictionaries into one dictionary, with the keys being username"""
    return_dict = {}
    for user_info in user_info_dicts:
        username = user_info['subTitle'][1:]
        return_dict[username] = clean_user_dict(user_info)

    return return_dict

def sound_list_to_dict(sound_info_dicts):
    return_dict = {}
    for sound_info in sound_info_dicts:
        sound_name = sound_info['title']
        return_dict[sound_name] = {}

        for info_field in ['id','title','subTitle','description']:
            return_dict[sound_name][info_field] = sound_info[info_field]
        for info_field in ['posts']:
            return_dict[sound_name][info_field] = sound_info['extraInfo'][info_field]

    return return_dict

def hashtag_list_to_dict(hashtag_info_dicts):
    return_dict = {}
    for hashtag_info in hashtag_info_dicts:
        hashtag_name = hashtag_info['title']
        return_dict[hashtag_name] = {}

        for info_field in ['id','title','subTitle','description']:
            return_dict[hashtag_name][info_field] = hashtag_info[info_field]
        for info_field in ['views']:
            return_dict[hashtag_name][info_field] = hashtag_info['extraInfo'][info_field]

    return return_dict

def video_list_to_dict(video_info_dicts):
    """for a tiktok, return its metadata, hashtags, and sound"""
    return_dict = {}
    for video_info in video_info_dicts:
        video_id = video_info['id']
        return_dict[video_id] = {}

        for info_field in ['id','desc']:
            return_dict[video_id][info_field] = video_info[info_field]
        for info_field in ['id','title']: # load music info
            return_dict[video_id][f'music_{info_field}'] = video_info['music'][info_field]
        for info_field in ['diggCount','shareCount','commentCount','playCount']: # load stats info
            return_dict[video_id][f'stats_{info_field}'] = video_info['stats'][info_field]

        # mine hashtag
        caption_words = return_dict[video_id][info_field].split(' ')
        hashtags = []
        for word in caption_words:
            if word[0] == '#':
                hashtags.append(word[1:])
        return_dict[video_id]['hashtags'] = hashtags

    return return_dict


def fetch_user_info(user_dict, n_likes=10, n_videos=10, n_sugg_hashtags=10, n_sugg_sounds=10):
    """
    Fetch likes, suggested hashtags, suggested sounds, and videos (with their hashtags and sounds) from a given user.

    Keyword arguments:
    user_dict -- dictionary of 1 user's info
    n_likes -- number of likes to fetch, capped at ~2,000 (if public)
    n_videos -- number of videos to fetch, capped at ~2,000
    n_sugg_hashtags -- number of suggested hashtags to fetch
    n_sugg_sounds -- number of suggested sounds to fetch
    """    
    likes = api.userLiked(user_dict['id'], user_dict['secUid'], count=n_likes)

    sugg_hashtags = hashtag_list_to_dict(
        api.getSuggestedHashtagsbyID(count=n_sugg_hashtags, userId=user_dict['id'])
    )
    # print('#:')
    # print(sugg_hashtags)
    sugg_sounds = sound_list_to_dict(
        api.getSuggestedMusicbyID(count=n_sugg_sounds, userId=user_dict['id'])
    )
    # print('sounds:')
    # print(sugg_sounds)

    videos = video_list_to_dict(
        api.userPosts(user_dict['id'], user_dict['secUid'], count=n_videos)
    )   
    # print('vids:')
    # print(videos)

    return likes, sugg_hashtags, sugg_sounds, videos
    