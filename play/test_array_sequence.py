import unittest
from array_sequence import ArraySeq

class ArraySeqTest(unittest.TestCase):

    def setUp(self):
        """ Sets up a basic array sequence for testing different functioality"""
        X = [1,2,3,4]
        self.seq = ArraySeq()
        self.seq.build(X)
    
    def tearDown(self):
        """ Gets rid of the test array sequence after test is run"""
        self.seq = None

    def test_build(self):
        """given an iterable X, build sequence from items in X return the number of stored items"""

        # Arrange
        X = [1,2,3,4]
        seq = ArraySeq()
        # Act
        seq.build(X)
        # Assert
        self.assertEqual(seq.__len__(), len(X))

    def test_iter_seq(self):
        """ return the stored items one-by-one in sequence order""" 
        # Arrange
        X = [1,2,3,4]
        seq = ArraySeq()
        #Act
        seq.build(X)
        # Assert
        self.assertEqual(list(seq.__iter__()), [x for x in X])

        
    def test_copy_forward(self):
        new_array = 5*[None]
        self.seq._copy_forward(1,3,new_array,2)
        self.assertEqual(self.seq.get_at(1), new_array[2])
        self.assertEqual(self.seq.get_at(2), new_array[3])
        self.assertEqual(self.seq.get_at(3), new_array[4])

    def test_get_at(self):
        """return the ith item"""
        self.assertEqual(self.seq.get_at(1), 2)

    def test_set_at(self):
        """ replace the ith item with x """
        self.seq.set_at(1, 123)
        self.assertEqual(self.seq.get_at(1), 123)

    def test_insert_at(self):
        """ add x as the ith item"""
        self.seq.insert_at(1,12)
        self.assertEqual(self.seq.get_at(1), 12)

    def test_delete_at(self):
        """ remove and return the ith item"""
        self.seq.delete_at(1)
        self.assertEqual(list(self.seq.__iter__()), [1,3,4])

    def test_insert_first(self):
        """ add x as the first item"""
        self.seq.insert_first(999)
        self.assertEqual(self.seq.get_at(0), 999)

    def test_delete_first(self):
        """ remove and return the first item"""
        self.seq.delete_first()
        self.assertEqual(self.seq.get_at(0), 2)

    def test_insert_last(self):
        """ add x as the last item"""
        self.seq.insert_last(999)
        self.assertEqual(self.seq.get_at(len(self.seq)-1), 999)
    
    def test_delete_last(self):
        """ remove and return the last item """
        self.seq.delete_last()
        self.assertEqual(self.seq.get_at(len(self.seq)-1), 3)

if __name__ == "__main__":
    unittest.main()
