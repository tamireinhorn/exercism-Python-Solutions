def maximum_value(maximum_weight: int, items: list[dict[str, int]]):
    if not items:
        return 0 # No items, no money.
    # Solving via Dynamic Programming.
    n =len(items) # number of items
    # Create 2d array, with n+1 rows for items and w+1 columns for all weights.
    V = [[0 for i in range(maximum_weight+1)] for j in range(n+1)]
    # Build the sub problem table bottom down.
    # This table has a column for every capacity
    # And the row represents item i and its previous, in the order of the items list.
    # So every cell of the table is a subproblem, where we are solving a knapsack of weight w and items 0 to i.
    for i in range(n+1):
        item_weight = items[i-1]['weight']
        item_value = items[i-1]['value']
        
        for w in range(maximum_weight+1):
            # If you didn't pick the item, it's the subproblem a row above (without item i), same column because av capacity is the same
            not_pick_item = V[i-1][w]
            if i == 0 or w == 0: # If the item is empty or the knapsack fits nothing more:
                V[i][w] = 0 # Row, column is 0.
            # Next, check if the item fits:
            elif item_weight <= w:
                # If you pick the item, it's the row above discounting the capacity from the chosen item's weight + item's value
                pick_item = V[i-1][w - item_weight] + item_value
                V[i][w] = max(not_pick_item, pick_item)
            else:
                # If it doesn't fit, you can only not pick the item, and thus:
                V[i][w] = not_pick_item
    return V[n][maximum_weight] # The last cell is the true problem to be solved.