import unittest

import sys
sys.path.append('/home/yrian/repos/AOIS3')

from src.reducer.table_method.karnauhg_map.karnaugh_map_ceil import KarnaughMapCeil
from source.unimportant_karnaugh_map_ceil import UnimportantKarnaughMapCeil
from source.karnaugh_map_with_importance import KarnaughMapWithImportance

class TestKarnaughMapWithImportance(unittest.TestCase):
    def setUp(self):
        self.karnaugh_map = KarnaughMapWithImportance()

    def test_is_full_of_true(self):
        self.karnaugh_map.append([KarnaughMapCeil(True), KarnaughMapCeil(True)])
        self.karnaugh_map.append([UnimportantKarnaughMapCeil(), KarnaughMapCeil(True)])
        self.assertTrue(self.karnaugh_map.is_full_of_true())

    def test_is_full_of_false(self):
        self.karnaugh_map.append([KarnaughMapCeil(False), UnimportantKarnaughMapCeil()])
        self.karnaugh_map.append([KarnaughMapCeil(False), UnimportantKarnaughMapCeil()])
        self.assertTrue(self.karnaugh_map.is_full_of_false())

    def test_remove_useless_edges(self):
        ceils = [
            [KarnaughMapCeil(True), KarnaughMapCeil(True), UnimportantKarnaughMapCeil(), KarnaughMapCeil(False)],
            [KarnaughMapCeil(True), UnimportantKarnaughMapCeil(), UnimportantKarnaughMapCeil(), KarnaughMapCeil(True)],
        ]
        parent_map = KarnaughMapWithImportance()
        parent_map.append(ceils[0])
        parent_map.append(ceils[1])

        edges = [
            KarnaughMapWithImportance(parent_map),
            KarnaughMapWithImportance(parent_map),
            KarnaughMapWithImportance(parent_map),
        ]

        edges[0].append(ceils[1])

        edges[1].append(ceils[0][:2])
        edges[1].append(ceils[1][:2])

        edges[2].append(ceils[0][1:3])
        edges[2].append(ceils[1][1:3])

        expected_edges = [edges[0], edges[1]]

        self.assertEqual(self.karnaugh_map._remove_useless_edges(edges), expected_edges)


if __name__ == "__main__":
    unittest.main()
