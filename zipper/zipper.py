from functools import partial 

class Zipper(object):
    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def __init__(self, tree, parents = []) -> None:
        self.tree, self.parents = tree, parents
        #Loop over left, right and value
        for val in ('left', 'right', 'value'):
            # This will make self's attribute called set_val (left, right, value) as self.set(key = val, item)
            setattr(self, f'set_{val}', partial(self.set, val))
            setattr(self, val, partial(self.get, val))
            # Thus we created a setter and a getter for every attribute.

    def get(self, key):
        # If we are getting the value, we just get it straight up.
        if key == 'value':
            return self.tree['value']
        # If we are looking for left or right, we create a zipper of it, and the parents will be the original + the object itself. If the key doesn't existe we return nothing.
        return (Zipper(self.tree[key], self.parents + [self]) if self.tree[key] else None)
    
    def set(self, key, item):
        self.tree[key] = item
        return self.parents[0] if self.parents else self
    
    def up(self): 
        # This should return the upper node, so
        return self.parents[-1] if self.parents else None

    def to_tree(self):
        return self.parents[0].tree if self.parents else self.tree
