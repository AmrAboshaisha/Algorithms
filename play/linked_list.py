from linked_list_node import LinkedListNode as Node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def get_at(self, i):
        current_node = self.head
        next_node = current_node.next
        
        if current_node == None: return None
        else:
            idx = 0
            while idx != i:
                idx += 1
                current_node = next_node
                next_node = next_node.next
            return current_node

    def set_at(self, i, x):
        self.get_at(i).item = x

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

    def insert_at(self, i, x):
        node_to_replace = self.get_at(i)
        if node_to_replace == None:
            self.head = x
        else:
            if i == 0:
                self.head = x
                x.next = node_to_replace
            else:
                previous_node = self.get_at(i-1)
                previous_node.next = x
                x.next = node_to_replace

