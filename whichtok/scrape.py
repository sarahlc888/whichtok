# module with code to scrape data from TikTok
import pandas as pd
from TikTokApi import TikTokApi
import json
import subprocess 

api = TikTokApi()



class UserGroup:
    """Define a group of TikTok users and store their information

    Class includes functionality to scrape user information, store that info in CSV/JSON format, 
    and read info from previously scraped UserGroups.
    """
    users_dict = {} # a dictionary of user information (keys are usernames)
    
    # dictionaries to store information about hashtags and sounds (to remove repetitive info)
    hashtags = {} # hashtags[name of hashtag] = info
    sounds = {} # sounds[id of sound] = info
    videos = {}

    @staticmethod
    def load_from_json(json_file):
        json_stream = open(json_file, 'r')
        json_dict = json.load(json_stream)
        json_stream.close()
        return json_dict
    @staticmethod
    def load_from_csv(csv_file):
        return pd.read_csv(csv_file, sep='\t', index_col=0).to_dict('index')

    def __init__(self, seed_user=None, group_size=None, json_out_stem=None, json_in_stem=None, verbose=False):
        """load user group from dictionary or corresponding json"""
        if seed_user != None and group_size != None:
            suggested_n = crawl_user_set(seed_user, group_size)
            print(len(suggested_n))
            user_group_dict = {}
            for username in suggested_n:
                if verbose:
                    print(username)
                user_dict = suggested_n[username]

                sugg_hashtags = fetch_user_hashtags(user_dict, self.hashtags, verbose=verbose) # fetch hashtags for user and populate master list
                sugg_sounds = fetch_user_sounds(user_dict, self.sounds, verbose=verbose) # fetch sounds for user and populate master list
                user_videos = fetch_user_videos(user_dict, self.videos, verbose=verbose)
                likes = fetch_user_likes(
                    user_dict, n_likes=10, verbose=verbose
                )
                user_group_dict[username] = {}
                user_group_dict[username]['likes'] = likes
                user_group_dict[username]['sugg_hashtags'] = sugg_hashtags
                user_group_dict[username]['sugg_sounds'] = sugg_sounds
                user_group_dict[username]['videos'] = user_videos
                
            self.users_dict = user_group_dict

            if json_out_stem:
                subprocess.run(['mkdir','-p',json_out_stem])
                user_data_output = open(f'{json_out_stem}/users.json', 'w')
                json.dump(user_group_dict, user_data_output, indent='\t')
                user_data_output.close()
                
                pd.DataFrame(self.videos).transpose().to_csv(f'{json_out_stem}/videos.csv', sep='\t')

                pd.DataFrame(self.hashtags).transpose().to_csv(f'{json_out_stem}/hashtags.csv', sep='\t')
                # hashtag_output = open(f'{json_out_stem}/hashtags.json', 'w')
                # json.dump(self.hashtags, hashtag_output, indent='\t')
                # hashtag_output.close()
                
                pd.DataFrame(self.sounds).transpose().to_csv(f'{json_out_stem}/sounds.csv', sep='\t')
                # sound_output = open(f'{json_out_stem}/sounds.json', 'w')
                # json.dump(self.sounds, sound_output, indent='\t')
                # sound_output.close()

        elif json_in_stem:
            self.users_dict = self.load_from_json(f'{json_in_stem}/users.json')
            self.hashtags = self.load_from_csv(f'{json_in_stem}/hashtags.csv')
            self.sounds = self.load_from_csv(f'{json_in_stem}/sounds.csv')
            self.videos = self.load_from_csv(f'{json_in_stem}/videos.csv')

        else:
            raise 'Error: plase specify `json` or `seed_user` and `group_size`'
        
    def make_user_graph(self):
        """form a graph"""
        pass
    def make_video_graph(self):
        """form a graph"""
        pass


def crawl_user_set(seed_username, n):
    """
    Get a list of tiktok users from the given username.

    Keyword arguments:
    seed_username -- the user to use as a seed
    n -- number of users to fetch
    json_out -- optional output path to write user information to as JSON
    """

    seed_id = api.getUser(seed_username)['userInfo']['user']['id']
    suggested_n = api.getSuggestedUsersbyIDCrawler(count=n, startingId=seed_id)
    suggested_n = user_list_to_dict(suggested_n)

    return suggested_n
    
    # alternatively: suggested_n = pd.DataFrame(suggested_n).drop(['extraInfo','keyToken','playToken'], axis=1)

def clean_user_dict(user_info_dict):
    username = user_info_dict['subTitle'][1:]
    return_dict = {}

    for info_field in ['title','id','description']:
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





def fetch_user_hashtags(user_dict, hashtag_reference, n_sugg_hashtags=10, verbose=False):
    """
    Fetch suggested hashtags from a given user and update reference list
    
    Keyword arguments:
    user_dict -- dictionary of 1 user's info
    hashtag_reference -- running dictionary of hashtag information to update
    n_sugg_hashtags -- number of suggested hashtags to fetch
    """
    if verbose:
        print('...fetching #s')

    hashtag_info_dicts = api.getSuggestedHashtagsbyID(count=n_sugg_hashtags, userId=user_dict['id'])
    sugg_hashtag_ids = []

    for hashtag_info in hashtag_info_dicts: # loop through each hashag
        hashtag_name = hashtag_info['title']
        sugg_hashtag_ids.append(hashtag_name) # add hashtag to list attached to this user

        if hashtag_name in hashtag_reference:
            # if hashtag is already recorded, skip
            continue

        # otherwise, fetch the hashtag information
        hashtag_reference[hashtag_name] = {}

        for info_field in ['id','title','subTitle','description']:
            hashtag_reference[hashtag_name][info_field] = hashtag_info[info_field]
        for info_field in ['views']:
            hashtag_reference[hashtag_name][info_field] = hashtag_info['extraInfo'][info_field]

    return sugg_hashtag_ids

def fetch_user_sounds(user_dict, sound_reference, n_sugg_sounds=10, verbose=False):
    """
    Fetch suggested sounds from a given user and update reference list

    Keyword arguments:
    user_dict -- dictionary of 1 user's info
    sound_reference -- running dictionary of sound information to update
    n_sugg_sounds -- number of suggested sounds to fetch
    """    

    if verbose:
        print('...fetching sounds')

    suggested_sounds = api.getSuggestedMusicbyID(count=n_sugg_sounds, userId=user_dict['id'])

    sugg_sounds_ids = []

    for sound_info in suggested_sounds:
        sound_name = sound_info['title']
        sugg_sounds_ids.append(sound_name)

        if sound_name in sound_reference:
            continue

        sound_reference[sound_name] = {}

        for info_field in ['id','title','subTitle','description']:
            sound_reference[sound_name][info_field] = sound_info[info_field]
        for info_field in ['posts']:
            sound_reference[sound_name][info_field] = sound_info['extraInfo'][info_field]

    return sugg_sounds_ids

def fetch_user_videos(user_dict, video_reference, n_videos=10, verbose=False):
    """
    Fetch videos (with their hashtags and sounds) from a given user and update reference list

    Keyword arguments:
    user_dict -- dictionary of 1 user's info
    n_videos -- number of videos to fetch, capped at ~2,000
    """   

    if verbose:
        print('...fetching videos')
    user_videos = api.userPosts(user_dict['id'], user_dict['secUid'], count=n_videos)
    video_ids = []

    for video_info in user_videos:
        video_id = video_info['id']
        video_ids.append(video_id)

        if video_id in video_reference:
            continue

        video_reference[video_id] = {}

        for info_field in ['id','desc']:
            video_reference[video_id][info_field] = video_info[info_field]
        for info_field in ['id','title']: # load music info
            video_reference[video_id][f'music_{info_field}'] = video_info['music'][info_field]
        for info_field in ['diggCount','shareCount','commentCount','playCount']: # load stats info
            video_reference[video_id][f'stats_{info_field}'] = video_info['stats'][info_field]

        # mine hashtag
        caption_words = video_reference[video_id]['desc'].split(' ')
        hashtags = []
        for word in caption_words:
            if len(word)==0:
                continue
            if word[0] == '#':
                hashtags.append(word[1:])
        video_reference[video_id]['hashtags'] = hashtags

    return video_ids



def fetch_user_likes(user_dict, n_likes=10, verbose=False):
    """
    Fetch likes from a given user and update reference list

    Keyword arguments:
    user_dict -- dictionary of 1 user's info
    n_likes -- number of likes to fetch, capped at ~2,000 (if public)
    """    
    if verbose:
        print('...fetching likes')
    likes = api.userLiked(user_dict['id'], user_dict['secUid'], count=n_likes)

    return likes
    



## preliminary testing functions ##

# TODO: learn how to use unittest etc to do this test? come up with expected output values?

def test_UserGroup_():
    # test UserGroup initialization and output
    UserGroup(seed_user='tiktok', group_size=10, json_out_stem='temp_jsons', verbose=True)

    # test UserGroup initialization from previous outputs
    a = UserGroup(json_in_stem='temp_jsons')
    