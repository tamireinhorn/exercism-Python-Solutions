def tree_from_traversals(preorder, inorder):
    preorder_size, inorder_size = len(preorder), len(inorder)
    preorder_set, inorder_set = set(preorder), set(inorder)
    if len(preorder_set) != preorder_size or len(inorder_set) != inorder_size:
        raise ValueError('traversals must contain unique items')
    if preorder_size != inorder_size: 
        raise ValueError("traversals must have the same length")
    if preorder_set != inorder_set:
        raise ValueError("traversals must have the same elements")
    # The first item in preorder is the root.
    # So, with that, you go to in order.
    if not preorder or not inorder:
        return {}
    root = preorder[0]
    tree = {'v': root}
    # Then we get the root's position in the inorder
    root_position = inorder.index(root)
    breakpoint()