PLAYER_1 = 'X' # Left to right, starts at left edge, which is BETWEEN top and last rows.
PLAYER_2 = 'O' # top to bottom, starts at top ed
from copy import deepcopy
import re
from collections import namedtuple
node_info = namedtuple('NodeInfo', ['node', 'row', 'column'])


class Node:
    def __init__(self, value: str) -> None:
        self.value = value 
        self.is_visited = False 
    
    def visit(self) -> None:
        self.is_visited = True

    def is_valid(self, player: str) -> bool:
        return not self.is_visited and self.value == player


def create_node(value) -> Node:
    return Node(value)

class ConnectGame:
    def __init__(self, board: str) -> None:
        split_board = board.split('\n') # The board is a list of rows (also lists) whose elements are of the Node class.
        new_board = []
        spaces_to_add = 0
        end_spaces = len(split_board) -1
        for line in split_board:
            padding = list(map(lambda x: create_node('.'), range(spaces_to_add))) # Left padding to make it a rectangle
            padding += list(map(create_node, re.sub('\s', '', line)))
            padding += list(map(lambda x: create_node('.'), range(end_spaces))) # Also add right padding for it to be a rectange.
            new_board.append(padding)
            spaces_to_add += 1
            end_spaces -= 1
        self.board = new_board
        self.raw_board = board
        
    def get_winner(self) -> str:
        if self.player_victory(PLAYER_2):
            return PLAYER_2
        self.transpose_board() # If O is not the victor, only then do we need to test X by using the transposed board.
        if self.player_victory(PLAYER_1):
            return PLAYER_1
        return "" # If none of them win, then the winner is empty.

    def get_neighbor(self, row: int, column: int, player):
        # It's important to think about the hex board. Since we pad the board all around, the down left diagonal and upper right don't exist.
        # The rest do as if in a square.
        if player == PLAYER_1:
            board = self.transposed_board
        else:
            board = self.board
        row_edge = len(board)
        column_edge = len(board[row_edge - 1]) 
        neigh = []
        def add_valid_node(node): # This is just a helper function to verify that the node is valid, then visit it and add it to the neighbor list.
            if node.is_valid(player):
                node.visit()
                neigh.append(node_information)
        # This is just a series of border checks to guarantee that the neighboring node exists, and if so, append it to the neighbor list.
        if column != 0:
            node_information = node_info(board[row][column-1], row, column-1)
            node = node_information.node
            add_valid_node(node)
        if column != column_edge:
            node_information = node_info(board[row][column+1], row, column+1)
            node = node_information.node
            add_valid_node(node)
        if row != 0:
            node_information = node_info(board[row-1][column], row-1, column)
            node = node_information.node
            add_valid_node(node)
        if row != row_edge:
            node_information = node_info(board[row+1][column], row+1, column)
            node = node_information.node
            add_valid_node(node)
        if row != row_edge and column != column_edge:
            node_information = node_info(board[row+1][column+1], row+1, column+1)
            node = node_information.node
            add_valid_node(node)
        if row != 0 and column != 0:
            node_information = node_info(board[row-1][column-1], row-1, column-1)
            node = node_information.node
            add_valid_node(node)
        return neigh
        
    def player_victory(self, player) -> bool:
        if player == PLAYER_2:
            board = self.board # The top to bottom player can use the regular board.
        else:
            board = self.transposed_board # Whereas the other one, to make it easier, the board rotated 90 degrees.
        row_edge = len(board) - 1
        first_line = board[0]
        queue = [node_info(node, 0 ,i) for i, node in enumerate(first_line) if node.value == player]
        # My theoretical solution requires a queue, as if this is a graph:
        # We start from an initial node, then add it to the queue.
        # The algorithm works as follows: Dequeue from the queue.
        # The dequed node has neighbors (from that player and also not visited).
        # Enqueue them, rinse and repeat. 
        # The algorithm declares victory if it finds a node in the winning edge.
        # If the queue ends before it, that player did not win.
        while queue: # The algorithm is a breadth first search.
            first_of_the_queue = queue[0] # Get the first of the queue, which is a named tuple of row, column, node.
            row, column = first_of_the_queue.row, first_of_the_queue.column 
            board[row][column].visit() # Visit the given node.
            if row == row_edge: ## If we every visit a node that is on the edge of the board, the player won.
                return True
            queue = queue[1:] # Dequeue
            next_nodes = self.get_neighbor(row, column, player) # Get neighboring nodes to current one.
            queue += next_nodes # Add all of them to the queue.
        return False # After running through the queue, if there is nothing left, we never reached the edge and the player didn't win.

    def transpose_board(self) -> None:
        """ This method merely transforms the raw string of the board into a board of nodes, but transposed so that X's edges are now top and bottom.
        """
        board = self.raw_board
        transpose = []
        split_board = board.split('\n') # We split the board, like before.
        l = [re.sub('\s', '', line) for line in split_board] # We substitute the empty spaces.
        spaces_to_add = 0 # We have paddings as well.
        end_spaces = len(split_board) -1
        for line in zip(*l): # However, in this case, we transpose, so we unpack the list.
            # if l = ['OX', 'XO'], *l = [('O', 'X'), ('X', 'O')]
            # Thus, zip will pack together the ith items of the tuple, i.e, the columns, and thus transposes the board.
            padding = list(map(lambda x: Node('.'), range(spaces_to_add))) # Padding to the left
            padding += list(Node(val) for val in line) # Nodes for all those valid values.
            padding += list(map(lambda x: Node('.'), range(end_spaces))) # Padding to the right.
            transpose.append(padding)
            spaces_to_add += 1
            end_spaces -= 1
        self.transposed_board = transpose
