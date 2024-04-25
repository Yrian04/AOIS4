import unittest

import sys
sys.path.append('/home/yrian/repos/AOIS3')

from source.karnaugh_map_builder import KarnaughMapBuilder
from source.karnaugh_map_with_importance import KarnaughMapWithImportance



class KarnaughMapBuilderTests(unittest.TestCase):
    def setUp(self):
        self.builder = KarnaughMapBuilder()

    def test_build_with_valid_vector(self):
        vector = "00010110"
        result = self.builder.build(vector)

        self.assertIsInstance(result, KarnaughMapWithImportance)
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0]), 4)
        self.assertEqual(len(result[1]), 4)

        self.assertEqual(result._column_vars, ["x1"])
        self.assertEqual(result._row_vars, ["x2", "x3"])

        self.assertEqual(result[0][0].value, False)
        self.assertEqual(result[0][1].value, False)
        self.assertEqual(result[0][2].value, True)
        self.assertEqual(result[0][3].value, False)

        self.assertEqual(result[1][0].value, False)
        self.assertEqual(result[1][1].value, True)
        self.assertEqual(result[1][2].value, False)
        self.assertEqual(result[1][3].value, True)

    def test_build_with_invalid_vector_length(self):
        vector = "000101101"
        with self.assertRaises(ValueError):
            self.builder.build(vector)

    def test_build_with_invalid_vector_chars(self):
        vector = "00010u10"
        with self.assertRaises(ValueError):
            self.builder.build(vector)


if __name__ == "__main__":
    unittest.main()

