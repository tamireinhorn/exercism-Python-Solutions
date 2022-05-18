class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0

    def push(self, value):
        new_node = Node(value, previous = self.tail)
        if self.head: # List is not empty
            self.tail.succeeding = new_node #TODO: You need to make sure there is a previous node here. 
            self.tail = new_node 
        else:
            self.head = new_node
            self.tail = new_node 
        self.length += 1
        
    def pop(self):
        value_to_return = self.tail.value 
        self.tail = self.tail.previous 
        self.length -= 1
        return value_to_return

    def shift(self):
        value_to_return = self.head.value 
        self.head = self.head.succeeding
        self.length -= 1
        return value_to_return
    
    def unshift(self, value):
        new_node = Node(value, succeeding= self.head)
        if self.head:
            self.head.previous = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node 
        self.length += 1

    def __len__(self):
        return self.length # There is no decent reason for not cacheing this, is there? Lest we wanted to do the following


    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value 
            current_node = current_node.succeeding
        