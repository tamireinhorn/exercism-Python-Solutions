def tree_from_traversals(preorder: list, inorder: list):
    preorder_size, inorder_size = len(preorder), len(inorder)
    preorder_set, inorder_set = set(preorder), set(inorder)
    if len(preorder_set) != preorder_size or len(inorder_set) != inorder_size:
        raise ValueError('traversals must contain unique items')
    if preorder_size != inorder_size: 
        raise ValueError("traversals must have the same length")
    if preorder_set != inorder_set:
        raise ValueError("traversals must have the same elements")
    if not preorder or not inorder:
        return {}
    if preorder_size == 1:
        return {"v": preorder[0], "l": {}, "r": {}}
    #The first element of in-order will be the leftmost element of the tree.
    # In order will always go as much as it can to the left, then go left tree in order from left to right, then current node, then right.
    # Pre order will always go current, then left in pre order (current, left, right.) then right.
    # No matter what, pre order's first element is going to be the root.
    tree = process_tree(preorder, inorder)
    return tree

def process_tree(preorder: list[str], inorder: list[str]):
    # You get a preorder and a inorder list, a SUBSET of them.
    if not preorder:
        return {}
    root = preorder[0]
    if len(preorder) == 1:
        return {"v": root, "l": {}, "r": {}}
    # The left part will be everything in the inorder until the root element.
    root_location = inorder.index(root)
    left_inorder = inorder[:root_location]
    left_size = len(left_inorder) + 1
    left_preorder = preorder[1:left_size]
    right_inorder = inorder[root_location+1:]
    right_preorder = preorder[left_size:]
    # You do this recursively... until there is but one element
    tree = {"v": root, "l": process_tree(left_preorder, left_inorder), "r": process_tree(right_preorder, right_inorder)}
    return tree