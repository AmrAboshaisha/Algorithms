import unittest


class SortingAlgorithmsTests(unittest.TestCase):
    def setUp(self):
        A = []
        A_ = []
        B = [1]
        B_ = [1]
        C = [2, 1]
        C_ = [1, 2]
        D = [4, 5, 3]
        D_ = [3, 4, 5]
        E = [8, 2, 4, 9, 3]
        E_ = [2, 3, 4, 8, 9]

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


if __name__ == "__main__":
    unittest.main()
