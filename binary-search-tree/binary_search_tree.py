from collections import deque


class TreeNode:
    def __init__(self, value: int, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data: list[int]):
        self.root = None 
        for data in tree_data:
            self.insert_data(data)

    def data(self):
        return self.root

    def sorted_data(self):
        stack = []
        def inorder(node): # Recursive inner function that we just need to use for inorder traversal.
            if not node:
                return # If the node is null, we stop
            inorder(node.left) # We always go left as much as we can 
            stack.append(node.data) # Then we append to the variable in the upper scope
            inorder(node.right)
        inorder(self.root) # Call it starting from the root of the tree.
        return stack

    def insert_data(self, value_to_insert):
        new_node = TreeNode(value_to_insert)
        if not self.root: # If there is no root, we just start the tree with a node.
            self.root = new_node
            return 
            # So if there is already a root, what do we do?
        current_node = self.root
        while current_node: # We have to traverse the tree until we hit a null node.
            if value_to_insert > current_node.data: # A BST always follows the right for bigger left for smaller.
                if current_node.right:
                    current_node = current_node.right # We need to bubble down the tree until the null
                else:
                    current_node.right = new_node
                    break
            else: # Less or equal goes to the left subtree and bubbles down until avaliable.
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
    
    
                