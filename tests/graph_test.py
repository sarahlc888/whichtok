import unittest
import UserGraph
import UserGroup

class TestUserGraph(unittest.TestCase):
    def test_user_group(self):
        user_graph = UserGraph(UserGroup(json_in_stem='test_UserGroup_files'))
        
        # assert that the correct users are loaded
        self.assertEqual(
            ','.join(sorted(user_graph.user_list)),
            'dhar.mann,dunkin,ellendegeneres,mrbeast,netflix,thehypehouse,tiktokarab,tiktokcreators,tiktoknewsroom,willywonkatiktok'
        )        

        # assert that the graph has the correct number of nodes
        self.assertEqual(len(user_graph.graph.vs), 10)

        # assert that the graph has correct edges and edgeweights
        self.assertEqual(
            user_graph.graph.get_edgelist(),
            [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (5, 6), (5, 7), (5, 8), (5, 9), (6, 7), (6, 8), (6, 9), (7, 8), (7, 9), (8, 9)]
        )
        self.assertEqual(
            user_graph.graph.es['weight'],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.3333333333333333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3333333333333333, 0.0, 0.0]
        )

if __name__ == '__main__':
    unittest.main()