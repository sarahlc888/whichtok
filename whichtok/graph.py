from igraph import * # https://github.com/igraph/python-igraph
from scrape import UserGroup

class UserGraph:
    username_to_index = {}
    user_list = []


    def __init__(self, user_group):
        """form a graph of tiktok users from a UserGroup object"""

        # load users into UserGraph structures username_to_index and user_list
        for i,user in enumerate(user_group.users_dict.keys()):
            self.username_to_index[user] = i
            self.user_list.append(user)

        g = Graph()
        g.add_vertices(len(self.user_list))

        # print(g)
        # g.add_edges(edgelist)
        # print(g)
        # self.graph = g

UserGraph(UserGroup(json_in_stem='tiktok_jsons'))