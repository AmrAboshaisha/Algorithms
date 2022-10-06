import unittest 
from static_array import StaticArray

class TestStaticArray(unittest.TestCase):
    
    def test_static_array(self):
        # Arrange: arrange the data / state required for the function to work
        # here we instantiate a static array of size 10
        n = 10
        # Act: call the function / class method / etc
        array = StaticArray(10)
        array.set_at(0, 0)
        array.set_at(1, 1)
        array.set_at(2, 2)
        
        # Assert: verify the result
        self.assertIsInstance(array, StaticArray)
        self.assertEqual(array.get_at(1), 1)
        


if __name__ == "__main__":
    unittest.main()
