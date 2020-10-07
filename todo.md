## To Do
- [ ] scrape a representative set of users, their videos, and their likes. Save info as CSV to avoid unnecessary API calls
- [ ] Decide how to construct graphs
    - [ ] What python lib to use?
        - [ ] If applicable, decide how to represent videos and users (user and video classes or just rows in a dataframe)
    - [ ] Decide whether to work on the video or user level
    - [ ] What determines edgeweight?
        - User level: shared sounds, hashtags, likes?
        - Video level: shared sounds, hashtags, liked by same users?
    