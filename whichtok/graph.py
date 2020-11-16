from igraph import * # https://github.com/igraph/python-igraph
from .scrape import UserGroup

class UserGraph:
    """Represents TikTok users in a weighted undirected graph

    Weights edges between users by extent of user interaction, 
    measured through similarity of hashtags and sounds used
    (more methods coming soon).

    Attributes:
        username_to_index: a dictionary mapping each username to the appropriate integer
        user_list: a list of usernames, mapping each integer to the appropriate username
        graph: an igraph Graph object describing the group of users, where vertex i
          corresponds to user `user_list[i]`
    """
    username_to_index = {}
    user_list = []
    
    def __str__(self):
        layout = self.graph.layout("kk")
        plot(self.graph, layout = layout)
        return 'See graph png'

    def __init__(self, user_group, edge_criteria=['used_hashtags', 'used_sounds'], verbose=False):
        """Constructs a graph of tiktok users from a UserGroup object

        Construct edges using suggested hashtags, suggested sounds, 
        used hashtags, or used sounds. Store graph in `self.graph`.

        Args:
            user_group: a UserGroup object to transform into a graph
            edge_criteria: a list of strings representing how edge weights 
              will be determined
        """

        # load users into UserGraph structures username_to_index and user_list
        for i,user in enumerate(user_group.users_dict.keys()):
            self.username_to_index[user] = i
            self.user_list.append(user)

        if verbose:
            print(f'users: {self.user_list}')

        # initialize graph
        g = Graph()
        g.add_vertices(len(self.user_list))

        # calculate edge weights, pairwise
        edgelist = []
        weights = []
        for i in range(len(self.user_list)):
            for j in range(i+1, len(self.user_list)):

                # fetch dict of information about 2 users
                user1 = user_group.users_dict[self.user_list[i]]
                user2 = user_group.users_dict[self.user_list[j]]

                # loop through criteria
                edge_weight = UserGraph.calculate_edge_weight(user1, user2, edge_criteria)

                edgelist.append((i,j))
                weights.append(edge_weight)
        
        # load edges and weights into graph
        g.add_edges(edgelist)
        g.es['weight'] = weights
        g.es['label'] = weights

        self.graph = g

    @staticmethod
    def calculate_edge_weight(user1, user2, edge_criteria):
        """Calculates the edgeweight between two given users

        Args:
            user1: a dictionary of a user's information
            user2: a dictionary of another user's information
            edge_criteria: a list of strings representing how edge weight
              will be determined
        
        Returns:
            A float representing the appropriate edge weight
        """
        weight = 0
        for criteria in edge_criteria:
            if criteria in ['sugg_hashtags', 'sugg_sounds', 'used_hashtags', 'used_sounds']:
                # proportion of overlap, scaled by number of suggestions given (should be 9-10 total)
                weight += len(set(user1[criteria]).intersection(set(user2[criteria]))) / mean([len(user1[criteria]), len(user2[criteria])])
            elif criteria in ['TODO']:
                pass
        return weight
