

# <img src="https://cdn4.iconfinder.com/data/icons/social-media-flat-7/64/Social-media_Tiktok-512.png" width="30" height="30"> Whichtok <img src="https://cdn4.iconfinder.com/data/icons/social-media-flat-7/64/Social-media_Tiktok-512.png" width="30" height="30">
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code_of_conduct.md)



**Whichtok** is a library to construct social graphs from TikTok data. The library is currently a WIP, and [contributions](#contributions) are greatly appreciated.

## Installation & Quick Start
Install Whichtok and its dependencies with the package manager [pip](https://pip.pypa.io/en/stable/). Whichtok uses [`TikTok-Api`](https://davidteather.github.io/TikTok-Api/) to scrape video and user data from TikTok and [`igraph`](https://github.com/igraph/python-igraph) for graph construction and manipulation, along with its dependency [`cairocffi`](https://www.cairographics.org/).
```
pip3 install whichtok TikTokApi python-igraph cairocffi
```

Get started with Whichtok by scraping 10 users from the default seed and constructing and visualizing the corresponding graph:
```python
import whichtok
users = whichtok.UserGroup(seed_user='tiktok', group_size=10)
user_graph = UserGraph(users)
print(user_graph)
```

## Why Whichtok?
Social media platforms like Instagram and Twitter match people to content using a **follower graph**—users follow other users to tailor their feed to their preferences. While TikTok does offer a 'follow' feature, the platform primarily uses its [**For You page**](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you) to learn what content users are interested in and deliver similar content to their feeds.

TikTok's algorithm trains itself using signals such as whether a user likes a video or how much time a user spends watching it. It thus constructs **interest graphs** based on users' subconscious desires. (See this [article](https://www.eugenewei.com/blog/2020/8/3/tiktok-and-the-sorting-hat) by Eugene Wei for further discussion.) The For You page has won TikTok a massive following and helped partition the platform into its many subcultures or niches, which fall under the umbrella of ‘alt TikTok’ and prize themselves as elusive and/or oddly specific. 

Whichtok will enable developers to ask questions like how does a social media platform based on interest graphs group people into subcultures? What niches exist on TikTok? What does ‘membership’ in different communities look like? Does TikTok’s partitioning of users into subcultures limit and constrict discourse or simply help people find a shared space?

## How does it work?
In Whichtok's graphs, each user is a node and the weight of an edge between two users approximating the extent to which they ‘share space’ on TikTok (i.e. interact with each other and the amount and interact with the same content). Applying network analysis algorithms to this graph enables an investigation of TikTok’s social landscape.

## Contributions
[CONTRIBUTING.md](CONTRIBUTING.md) contains contribution guidelines and the tasks and features which I'm currently working on.  

## License
[MIT](https://choosealicense.com/licenses/mit/)