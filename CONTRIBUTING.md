# Contributing
## Getting Started
Once you familarize yourself with the [README](README.md) and install whichtok's dependencies, you are ready to start contributing.
## Pull Requests
Please make pull requests to the `develop` branch. The `main` branch should always hold fully functional code, and features from the `develop` branch will be merged in as they become ready with the `--no-ff` flag to require merge commits and avoid losing information about the development process.

## Project Roadmap
Feel free to take on any of these tasks. They are in a rough form right now, but more detailed descriptions are coming soon.

- [ ] crawl to fetch a representative set of users, their last 1000 videos, and their last 1000 likes. Save info as CSV/json to avoid unnecessary API calls
    - [ ] Decide how to represent videos and users (user and video classes? or just rows in a dataframe?)

- [ ] Construct graphs (note: there are 4 elements at play: users who post, posts that are liked, hashtags used, sounds used. A graph of any one of these elements can use the other 3 to determine edgeweights.)

    - [ ] construct user level graphs
        - [ ] simplest case: build a graph of users using the getSuggestedUser links
        - [ ] assemble a graph of users based on likes (the past 1000 likes)
        - [ ] shared sounds
        - [ ] shared hashtags
    - [ ] construct video level graphs within a pool of certain users
        - then can color by the user who made it
        - [ ] based on if the same person liked it
        - [ ] shared sounds
        - [ ] shared hashtags
    - [ ] construct hashtag level graphs. Implement edgeweights:
        - [ ] based on if the same user uses it
        - [ ] shared sound
        - [ ] shared like
    - [ ] construct sound level graphs
        - [ ] based on if the same user uses it
        - [ ] shared hashtag
        - [ ] shared like


## Code of Conduct
Note that this library has a [Code of Conduct](CODE_OF_CONDUCT.md), the widely adopted [Contributor Covenant](https://www.contributor-covenant.org/). Please be sure to follow it in order to keep whichtok a welcoming and inclusive community.