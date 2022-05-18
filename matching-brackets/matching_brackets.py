OPENINGS_DICT = {'}': '{', ')': '(', ']': '['}
CLOSINGS = list(OPENINGS_DICT.keys())
OPENINGS = list(OPENINGS_DICT.values())

def is_paired(input_string):
    # The gist of this is, you build a stack of the openings:, like  (, [, {. 
    openings_stack = []
    for element in input_string:
        if element in OPENINGS:
            openings_stack.append(element)
        elif element in CLOSINGS:
           # When you have a closing element, you expect it match the closing of the last item in the stack
            if (openings_stack) and (openings_stack[-1] == OPENINGS_DICT.get(element)):
               openings_stack.pop() # Then you remove the item from the stack 
            else:
                return False # If this fails even once, it's unbalanced.
    return len(openings_stack) == 0 # If we emptied the stack, we have a balanced string.
