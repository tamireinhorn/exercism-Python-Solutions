from copy import copy
class Node:
    def __init__(self, value, next_node = None):
        self.__value = value
        self._next_node = next_node # Doubt: If I used this with __ I can't test it or set it in the linked list class? or do i do a setter?

    def value(self):
        return self.__value

    def next(self):
        return self._next_node


class LinkedList:
    def __init__(self, values=[]):
        self.__head = None
        self.__tail = None 
        self.__size  = 0 # We want to have a cache for the length. 
        if values:
            for value in values:
                self.push(value)
    
    def __massage_index(self, node_number):
        # This is just to allow for negative indices. 
        l = len(self)
        if node_number < 0:
            node_number = l + (node_number + 1)
        if l -1 < node_number:
            raise IndexError(f'The list has only {l} nodes, the node of number {node_number} doesn\'t exist.')
        return node_number

    def __len__(self):
        return self.__size # No need to calculate len EVERYTIME, right? 

    def head(self):
        if self.__head:
            return self.__head
        else:
            raise EmptyListException('The list is empty.')

    def tail(self):
        if self.__head:
            return self.__tail 
        else:
            raise EmptyListException('The list is empty')

    def push(self, value):
        # In reality, this operates like a stack.
        if not self.__head:
            # This is an empty list, so head and tail are the same guy, the new node.
            self.__head = self.__tail = Node(value)
        else:
            # If the list is not empty, we:
            new_node = Node(value, self.__head) # Create a node pointing to head
            self.__head = new_node  # Now reassign head to be the most recent guy. It's a stack, remember!
        self.__size += 1 # We can cache the len and just add 1 whenever we push. 

    def pop(self):
        # This returns the last item AND takes it out of the list. 
        # Which means I need to say that the head is now the following guy.
        if not self.__head:
            raise EmptyListException('The list is empty.')
        t = self.__head
        self.__head = self.__head._next_node
        self.__size -= 1
        return t.value()

    def __getitem__(self, index):
        if not self.__head:
            raise EmptyListException('The list is empty.')
        index = self.__massage_index(index)
        if index == 0: # If we ask for the first item, it's just the head.
            return self.head().value()
        # If not, we have to walk through the linked list. This could be done with __iter, but wouldn't make me learn.
        counter = 0
        current_node = self.__head # Start with the head.
        counter += 1 # Walk one step.
        while counter < index: # We will keep walking until we've walked {n} steps, where n is index.
            current_node = current_node._next_node 
            counter +=1
        return current_node.value() # Then we return the nth guy.

    def __iter__(self):
        current_node = self.__head # Start with the top of the list
        while current_node: # While we have a node
            yield current_node.value()  # yield is going to store the value and only give it when called. We store the value of the node.
            current_node = current_node._next_node # And we advance.
        return # Once the loop is done, we want to break out of the method.
    
    def reversed(self):
        # How do I reverse a linked list? 
        # Well, the tail must reference the node before it as the next.
        # And so on and so forth. So you need to have two pointers moving about like this
        # OBS: This could be done with __iter but wouldn't help me to learn the concepts.
        reversed_list = copy(self) # We don't want to modify the object.
        h = reversed_list.__head # Save the current head node. This will be the tail later on.
        if reversed_list.__head: # We can only reverse if it's not empty. 
            current_node = reversed_list.__head # Start with a pointer in the first node, the head.
            next_guy = current_node.next() # Get a second pointer for the sucessor.
            current_node._next_node = None # To avoid a loop, the head node must lose its edge to the next node.
            while next_guy: # This only runs while next_guy is a node. This is because we are always looking at the node i and its sucessor.
                # If there is no sucessor, we are at the end of the list and can stop.
                temp = copy(next_guy.next()) # We need to keep a pointer for node i + 2, for the following iteration should we need it.
                # This is because for 3 -> 2 -> 1, if we first change 2 -> 3, we never reach node 1, so we gotta point to it BEFORE changing.
                next_guy._next_node = current_node # Now, we invert part of the list, pointing node i + 1 to node i instead. 
                current_node = next_guy # Now we just walk ahead to the next iteration. 
                next_guy = temp 
            reversed_list.__tail = h # After looping, our previous head is now our tail (which ensures no cycles)
            reversed_list.__head = current_node # The last node we worked with is the last one on the original list (and thus the first one for reverse)
        return reversed_list 

class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
    
