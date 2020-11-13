# Contribution guidelines
## Getting Started
Once you familarize yourself with the [README](README.md) and install whichtok's dependencies, you are ready to start contributing.
## Pull Requests
Please make pull requests to the `develop` branch. The `main` branch should always hold fully functional code, and features from the `develop` branch will be merged in as they become ready, using the `--no-ff` flag to require merge commits and avoid losing information about the development process.

## What to work on
Check out GitHub [issues](https://github.com/sarahlc888/whichtok/issues) for tasks that I'm seeking help on. If you're interested in making a different contribution, open your own issue–I'd welcome any ideas!

## Documentation
Whichtok uses [Google-style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) comments and docstrings. Here's an example of a function docstring:
```
def example_func(test_arg):
    """Brief description of what example_func() does

    More detailed description, if necessary

    Args:
        test_arg: a [variable type] representing [variable significance]
    
    Returns:
        A [variable type] representing [variable significance]
    """
```

## Feeling lost? Here is a more technical project overview
To pair with the [README](README.md)'s overview of Whichtok's objectives and methodology, here are descriptions of the 3 main functionalities of Whichtok in slightly more technical terms to guide and ground your contributions to the library.

### 1. User scraping
Before jumping into analysis, Whichtok must obtain TikTok data.
Whichtok's [`UserGroup`](https://github.com/sarahlc888/whichtok/blob/develop/whichtok/scrape.py) class uses the [`TikTok-Api`](https://davidteather.github.io/TikTok-Api/)'s `getSuggestedUsersbyIDCrawler()` function to scrape video and user data and then stores it in the form of JSONs and CSVs.

The work to be done in this area is detailed in [this issue](https://github.com/sarahlc888/whichtok/issues/4). Primary challenges include overcoming API rate limiting and constructing a truly representative set of users.

### 2. Graph construction
Once obtaining user and video data, Whichtok can begin creating graphs. 
A graph is composed of nodes and edges and can be used to model and analyze many systems, including social media platforms.
Whichtok uses the [`igraph`](https://github.com/igraph/python-igraph) library for efficient graph construction and manipulation. At the moment, it focuses on *user-level* graphs in the [`UserGraph`](https://github.com/sarahlc888/whichtok/blob/develop/whichtok/graph.py) class. Each node in the graph represents a TikTok user (whose information was scraped in the previous step), and nodes are connected by edges with weight determined by the amount of interaction between users. For example, an edgeweight could increase if one user liked or commented on another user's video or if two users posted TikToks using the same sound or hashtag.

The work to be done is this area is that there's currently no way to determine user likes, removing an important method of graph construction (see [this issue](https://github.com/sarahlc888/whichtok/issues/5)). Finding alternative means or leveraging available information to construct meaningful graphs is a high priority.

Note: *Video-level* graphs are another potential type of graph within Whichtok. They have not yet been implemented, but could be implemented in a fashion similar to `UserGraph`, with the edgeweight between two videos determined by whether videos share a sound, hashtag, like from the same user, etc.

### 3. Graph analysis
The heart of Whichtok will lie in its graph analysis functionalities. Whichtok will use community detection algorithms from graph theory to understand how TikTok partitions users into niches on the platform. Potential visualizations could also uncover patterns in the hashtags, sounds, effects, etc. used by users in certain corners of TikTok compared to others to determine how trends on TikTok spread and how disparate communities interact. However, plans in this domain are much more fluid than in the previous two, and suggestions are more than welcome.

## Code of Conduct
This library has a [Code of Conduct](CODE_OF_CONDUCT.md), the widely adopted [Contributor Covenant](https://www.contributor-covenant.org/). Please be sure to follow it in order to keep whichtok a welcoming and inclusive community.