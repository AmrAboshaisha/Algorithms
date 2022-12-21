import unittest
from linked_list import Linked_List_Node as Node
from linked_list import Linked_List_Seq as LinkedList
from reorder import *

class ReorderStudentsTest(unittest.TestCase):

    def setUp(self):
        self.students = LinkedList()


    def test_reorder(self):
        x = ['A', 'B', 'C', 'D', 'E', 'F']
        self.students.build(x)
        # Act
        reorder(self.students)
        # Assert
        self.assertEqual(list(self.students), ['A', 'B', 'C', 'F', 'E', 'D'])



if __name__ == "__main__":
    unittest.main()

