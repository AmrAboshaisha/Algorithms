import unittest
from linked_list_node import LinkedListNode

class LinkedListNodeTest(unittest.TestCase):
    def test_linked_list_node(self):
        # Arrange
        node = LinkedListNode()
        # Act and Assert
        self.assertEqual(node.item, None)
        self.assertEqual(node.next, None)


if __name__ == "__main__":
    unittest.main()
