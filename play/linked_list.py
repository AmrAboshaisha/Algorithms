from linked_list_node import LinkedListNode as Node

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def __len__(self):
        return self.size

    def get_at(self, i):
        current_node = self.head
        next_node = None 
        
        idx = 0
        while idx != i:
            next_node = current_node.next
            current_node = next_node
            idx += 1

        return current_node

    def set_at(self, i, x):
        self.get_at(i).item = x

    def insert_first(self, x):
        if self.head == None: 
            self.head = x
        else:
            x.next = self.head
            self.head = x
        
        self.size +=1

    def delete_first(self):
        if self.head == None: pass
        else:
            first_node = self.head
            second_node = first_node.next
            self.head = second_node
            return first_node
        self.size -=1
        
    def insert_at(self, i, x):
        if i == 0:
            first_node = self.head
            self.head = x
            x.next = first_node

        else:
            current_node = self.get_at(i)
            previous_node = self.get_at(i-1)
            x.next = current_node
            previous_node.next = x

        self.size +=1

    def delete_at(self, i):
        if i == 0:
            current_node = self.get_at(i)
            next_node = current_node.next
            current_node.next = None
            self.head = next_node
        else:
            previous_node = self.get_at(i-1)
            current_node = previous_node.next
            next_node = current_node.next

            previous_node.next = next_node
            current_node.next = None
 
        self.size -=1
