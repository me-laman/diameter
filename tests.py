import unittest
from .graph_diameter import bfs_paths, shortest_path, get_vertices, diameter

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G']
}

graph2 = {
    '1': ['2'],
    '2': ['1', '3', '4', '5'],
    '3': ['2'],
    '4': ['2', '7'],
    '5': ['2', '6'],
    '6': ['5'],
    '7': ['4']
}


class TestBfsPaths(unittest.TestCase):

    def test_list_of_path_ok(self):
        lp = list(bfs_paths(graph, 'A', 'F'))
        lp2 = list(bfs_paths(graph, 'C', 'E'))

        self.assertEqual(lp, [['A', 'C', 'F'], ['A', 'B', 'E', 'F']])
        self.assertEqual(lp2, [['C', 'F', 'E'], ['C', 'A', 'B', 'E']])

    def test_shortest_of_path_ok(self):
        lp = list(shortest_path(graph, 'A', 'F'))
        lp2 = list(shortest_path(graph, 'C', 'E'))

        self.assertEqual(lp, ['A', 'C', 'F'])
        self.assertEqual(lp2, ['C', 'F', 'E'])

    def test_count_vertices_ok(self):
        vertices = get_vertices(graph)
        vertices.sort()

        self.assertEqual(vertices, ['A', 'B', 'C', 'D', 'E', 'F'])


class TestDiameter(unittest.TestCase):

    def test_diameter_G1(self):

        d1, path1 = diameter(graph)
        self.assertIn(path1, [['C', 'A', 'B', 'D'], ['D', 'B', 'A', 'C'], ['D', 'B', 'E', 'F'], ['F', 'E', 'B', 'D']])
        self.assertEqual(d1, 4)

    def test_diameter_G2(self):

        d2, path2 = diameter(graph2)

        self.assertIn(path2, [['6', '5', '2', '4', '7'], ['7', '4', '2', '5', '6']])
        self.assertEqual(d2, 5)


if __name__ == '__main__':
    unittest.main()