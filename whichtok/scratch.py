import pandas as pd
from TikTokApi import TikTokApi
api = TikTokApi()


def get_trending(n):
    """testing the API, pulled directly from quick start https://davidteather.github.io/TikTok-Api/#the-by-username-method"""
    trending = api.trending(count=n)

    for tiktok in trending:
        # Prints the text of the tiktok
        print(tiktok['desc'])

    print(len(trending))


def fetch_repr_set(seed_user, n):
    """Fetch a representative set of tiktok users from the given seed.

    Keyword arguments:
    seed_user -- the user to use as a seed
    n -- number of users to fetch
    """
    tiktok_id = api.getUser('tiktok')['userInfo']['user']['id']
    suggested_100 = api.getSuggestedUsersbyIDCrawler(count=100, startingId=tiktok_id)
    suggested_100 = pd.DataFrame(suggested_100).drop(['extraInfo','keyToken','playToken'], axis=1)
    # TODO: load these users into the desired data structure

def fetch_user_info(username, user_id, n):
    """Fetch likes, hashtags from a given user.

    Keyword arguments:
    username -- the user
    user_id -- the user id
    n -- number of likes to fetch
    """
    api.userLikedbyUsername(username, count=n)
    api.getSuggestedHashtagsbyID(count=n, userId=user_id)
    # TODO: load the likes and hashtags into the graph
