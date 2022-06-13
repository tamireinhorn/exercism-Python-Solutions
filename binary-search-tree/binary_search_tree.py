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
        self.root = self.recursive_method(value_to_insert, self.root)

    def recursive_method(self, value, node: TreeNode):
        # This method essentially bubbles down following the standard rules, until it finds a leaf node, then places the new node properly.
        # Then, the recursion back needs that we return the current node.
        # Imagine you already have a tree like:
        # 2 <- 4 -> 6
        # And now you need to insert 1, which would be to the left of 2, naturally. 
        # So you start the method at the root (4), go down to the else, call the method again. Now node is 2, and we go to the else again.
        # Since it's left is null, we go return TreeNode(1), which recurses up, making node 2's left that Node(1). HOWEVER, if it just stopped here...
        # 4 would have lost its left. So after we did 1 <- 2, we need to return 2 because it will recurse up to make 2 <- 4, therefore maintaining the tree.
        # This is, in a nutshell, why you need the last return. 
        if not node: # Once we find a leaf node, we return a created node. 
            return TreeNode(value)
        if value > node.data:
            node.right = self.recursive_method(value, node.right) # Bubble down one level. 
        else:
            node.left = self.recursive_method(value, node.left)
        return node # You always need to return the current node so that when you bubble down the previous nodes remain in place.
