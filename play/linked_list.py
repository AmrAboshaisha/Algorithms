from linked_list_node import LinkedListNode as Node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_first(self, x):
        if self.head == None: self.head = x
        else:
            first_node = self.head
            self.head = x
            x.next = first_node

    def delete_first(self):
        if self.head == None: pass
        else:
            first_node = self.head
            second_node = first_node.next
            self.head = second_node
            return first_node
