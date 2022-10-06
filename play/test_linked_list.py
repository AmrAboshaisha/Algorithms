import unittest
from linked_list_node import LinkedListNode as Node
from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    
    def test_non_empty_linked_list(self):
        first_node = Node(item="First Node")
        llist = LinkedList(head=first_node)
        self.assertEqual(llist.head, first_node)

    def test_insert_first(self):
        # Arrange
        first_node = Node(item="First Node")
        llist = LinkedList(head=first_node)
        second_node = Node(item="Second Node")
        # Act
        llist.insert_first(second_node)
        # Assert
        self.assertEqual(llist.head, second_node)
        self.assertEqual(second_node.next, first_node)

    def test_delete_first(self):
        # Arrange
        first_node = Node(item="First Node")
        llist = LinkedList(head=first_node)
        # Act
        llist.delete_first()
        # Assert
        self.assertEqual(llist.head, None)
        
        # Another case with 2 nodes
        first_node = Node(item="First Node")
        second_node = Node(item="Second Node")
        first_node.next = second_node
        llist = LinkedList(head=first_node)
        llist.delete_first()
        self.assertEqual(llist.head, second_node)

if __name__ == "__main__":
    unittest.main()
