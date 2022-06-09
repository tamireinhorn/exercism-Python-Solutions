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
        self.size = len(tree_data)

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
        inorder(self.root) # Call it above.
        return stack

    def insert_data(self, value_to_insert):
        if not self.root:
            self.root = TreeNode(value_to_insert)
        else:
            # So if there is already a root, what do we do?
            current_node = self.root
            while current_node.data:
                if value_to_insert > current_node.data:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = TreeNode(value_to_insert)
                        break
                else:
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = TreeNode(value_to_insert)
                        break
    
    
                