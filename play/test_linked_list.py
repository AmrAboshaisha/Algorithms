import unittest
from linked_list_node import LinkedListNode as Node
from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    
    def setUp(self):
        self.first_node = Node(item="First Node")
        self.second_node = Node(item="Second Node")
        self.llist = LinkedList(head=self.first_node)
    
    def test_len(self):
        # Case1: one node
        llist = LinkedList()
        llist.insert_at(0, self.first_node)
        self.assertEqual(len(llist), 1)
        # Case2: 2 nodes
        llist = LinkedList()
        llist.insert_first(self.first_node)
        llist.insert_at(1, self.second_node)
        self.assertEqual(len(llist), 2)
        # Case3: Empty list
        llist = LinkedList()
        self.assertEqual(len(llist), 0)

    def test_non_empty_linked_list(self):
        self.assertEqual(self.llist.head.item, "First Node")

    def test_insert_first(self):
        # Act
        self.llist.insert_first(self.second_node)
        # Assert
        self.assertEqual(self.llist.head, self.second_node)
        self.assertEqual(self.second_node.next, self.first_node)

    def test_delete_first(self):
        # Act
        self.llist.delete_first()
        # Assert
        self.assertEqual(self.llist.head, None)
       
    def test_delete_first_2(self):
        # Another case with 2 nodes
        self.first_node.next = self.second_node
        self.llist.delete_first()
        self.assertEqual(self.llist.head, self.second_node)
    
    def test_insert_at(self):
        self.first_node.next = self.second_node
        new_node = Node(item="New Node")

        # Act
        self.llist.insert_at(1, new_node)

        # Assert
        self.assertEqual(self.llist.get_at(1), new_node)

    def test_get_at(self):
        self.first_node.next = self.second_node
        third_node = Node(item="Third Node")
        self.llist.insert_at(2, third_node)
        #self.second_node.next = third_node
        self.assertEqual(self.llist.get_at(0), self.first_node)
        self.assertEqual(self.llist.get_at(1), self.second_node)
        self.assertEqual(self.llist.get_at(2), third_node)
    
    def test_set_at(self):
        self.llist.set_at(0, "Changed First Node")
        self.assertEqual(self.first_node.item, "Changed First Node")

    def test_delete_at(self):
        #Case 1: delete from 0th node
        self.llist.insert_at(1, self.second_node)
        self.llist.delete_at(0)
        self.assertEqual(self.llist.head.item, "Second Node")
        # Case 2: delete from last node
        llist = LinkedList(head=self.first_node)
        self.first_node.next = self.second_node
        llist.delete_at(1)
        self.assertEqual(llist.head.next, None)
        # Case 3: delete from middle node
        llist = LinkedList(head=self.first_node)
        self.first_node.next = self.second_node
        third_node = Node(item="Third Node")
        self.second_node.next = third_node
        llist.delete_at(1)
        self.assertEqual(llist.get_at(1), third_node)

if __name__ == "__main__":
    unittest.main()
