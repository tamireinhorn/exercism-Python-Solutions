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
        self.recursive_method(value_to_insert, self.root)
        
    def recursive_method(self, value_to_insert, current_node: TreeNode):
        if value_to_insert > current_node.data: # We got to go right.
            if not current_node.right:
                current_node.right = TreeNode(value_to_insert) 
            else:
                self.recursive_method(value_to_insert, current_node.right) # Bubble down right
        else:
            if not current_node.left:
                current_node.left = TreeNode(value_to_insert)
            else:
                self.recursive_method(value_to_insert, current_node.left) # Bubble down left
