import unittest
from sorting import *


class SortingAlgorithmsTests(unittest.TestCase):

    def setUp(self):
        self.A = []
        self.A_ = []
        self.B = [1]
        self.B_ = [1]
        self.C = [2, 1]
        self.C_ = [1, 2]
        self.D = [4, 5, 3]
        self.D_ = [3, 4, 5]
        self.E = [8, 2, 4, 9, 3]
        self.E_ = [2, 3, 4, 8, 9]

    def test_selection_sort(self):
        selection_sort(self.A)
        self.assertEqual(self.A, self.A_)
        selection_sort(self.B)
        self.assertEqual(self.B, self.B_)
        selection_sort(self.C)
        self.assertEqual(self.C, self.C_)
        selection_sort(self.D)
        self.assertEqual(self.D, self.D_)
        selection_sort(self.E)
        self.assertEqual(self.E, self.E_)

    def test_insertion_sort(self):
        insertion_sort(self.A)
        self.assertEqual(self.A, self.A_)
        print("Test 1 Finished")
        insertion_sort(self.B)
        self.assertEqual(self.B, self.B_)
        print("Test 2 Finished")
        insertion_sort(self.C)
        self.assertEqual(self.C, self.C_)
        print("Test 3 Finished")
        insertion_sort(self.D)
        self.assertEqual(self.D, self.D_)
        print("Test 4 Finished")
        insertion_sort(self.E)
        self.assertEqual(self.E, self.E_)
        print("Test 5 Finished")


if __name__ == "__main__":
    unittest.main()

if __name__ == "__main__":
    unittest.main()
