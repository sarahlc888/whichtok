# Whichtok
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](code_of_conduct.md)

**Whichtok** is a library to construct social graphs from TikTok data. The library is currently a WIP, and [contributions](#contributions) are greatly appreciated.

## Installation
Install Whichtok and its dependencies with the package manager [pip](https://pip.pypa.io/en/stable/):
```
pip3 install whichtok TikTokApi python-igraph cairocffi
```
Whichtok uses [`TikTok-Api`](https://davidteather.github.io/TikTok-Api/) to scrape video and user data from TikTok and [`igraph`](https://github.com/igraph/python-igraph) for graph construction and manipulation. [`cairocffi`](https://www.cairographics.org/) is a dependency of `igraph` necessary for graph visualizations.

## Why Whichtok?
Social media platforms such as Instagram and Twitter match people to content using a social graph. Users follow other users to view and interact with their posts and may adjust who follow to tailor their feed to their interests. Unlike other platforms, however, TikTok matches content to users using an *interest graph*.

TikTok does allow users to follow other users, but its primary feature is not a following feed. Instead, TikTok uses its [*For You page*](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you) to learn what content users are interested in and deliver similar content to user feeds. Through the For You page, TikTok constructs an interest graph without ever requiring explicit user direction. The algorithm is trained using signals such as whether a user likes a video or how much time a user spends watching it before swiping to the next one. The longer a user spends on TikTok, the more personalized the algorithm’s recommendations become, as the algorithm literally responds to the desires of their subconscious. Eugene Wei describes the effects of the TikTok For You page in more detail in this [blog post](https://www.eugenewei.com/blog/2020/8/3/tiktok-and-the-sorting-hat).

TikTok is able to pinpoint user preferences and deliver relevant content with such precision and accuracy that its algorithm has gained an air of mystique (compounded by a lack of popular understanding of its inner workings and lack of clarity and transparency on the part of TikTok—see [shadowbanning practices](https://www.bbc.com/news/technology-54102575) that have recently come to light). Anyhow, TikTok's unique FYP has won the app a massive following, and it is home to many subcultures or niches, entered via the FYP and governed by its influence. All fall under the umbrella term ‘alt TikTok’ and even prize themselves as obscure, oddly specific, and even elusive. 

Whichtok enables developers to examine such communities. By constructing and analyzing social graphs from user interactions, we can begin to ask questions like how does a social media platform based on interests group people into subcultures? What niches exist? To what extent does TikTok isolate different communities? How do users from different communities interact? What does ‘membership’ in different communities look like? Does TikTok’s partitioning of users into subcultures limit and constrict discourse or simply help people find a shared space?

## How does it work?
Whichtok scrapes data from TikTok users and constructs a corresponding graph. Graph functionalities are still under development, but each user will be represented as a node. The weight of an edge between two users will be determined by the amount that the users interact with each other and the amount that they interact with the same or similar content (approximating the extent to which they ‘share space’ on TikTok). Applying network analysis algorithms to this social graph can allow us to investigate TikTok’s social landscape.



## Contributions
[CONTRIBUTING.md](CONTRIBUTING.md) contains contribution guidelines and the tasks and features which I'm currently working on.  

## License
[MIT](https://choosealicense.com/licenses/mit/)