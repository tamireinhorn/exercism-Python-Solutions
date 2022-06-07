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
        
        answer = []
        # Start with a root. 
        # Then keep going left 
        current_node = self.root
        stack = [current_node]
        while len(answer) < self.size:
            while current_node.left:
                current_node = current_node.left 
                stack.append(current_node)
                breakpoint()
                # You've gone as LEFT as you can. Perfect. So now, we pop the stack, put it on order, then keep doing that until we can turn right. 
            while not current_node.right:
                current_node = stack.pop()
                answer.append(current_node.data)
                print(2)
            # Once we can turn right, we add THAT to the stack
            current_node = current_node.right 
            stack.append(current_node)
            # Then left until
        pass 

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
    
    
                