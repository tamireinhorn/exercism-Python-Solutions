PLAYER_1 = 'X' # Left to right, starts at left edge, which is BETWEEN top and last rows.
PLAYER_2 = 'O' # top to bottom, starts at top ed
from copy import deepcopy
import re
from collections import namedtuple
node_info = namedtuple('NodeInfo', ['node', 'row', 'column'])


class Node:
    def __init__(self, value: str):
        self.value = value 
        self.is_visited = False 
    
    def visit(self):
        self.is_visited = True

    def is_valid(self, player: str):
        return not self.is_visited and self.value == player


def create_node(value):
    return Node(value)

class ConnectGame:
    def __init__(self, board):
        split_board = board.split('\n')
        new_board = []
        spaces_to_add = 0
        end_spaces = len(split_board) -1
        for line in split_board:
            padding = list(map(lambda x: create_node('.'), range(spaces_to_add)))
            padding += list(map(create_node, re.sub('\s', '', line)))
            padding += list(map(lambda x: create_node('.'), range(end_spaces)))
            new_board.append(padding)
            spaces_to_add += 1
            end_spaces -= 1
        self.board = new_board
        self.raw_board = board
        
    def get_winner(self):
        if self.player_victory(PLAYER_2):
            return PLAYER_2
        self.transpose_board()
        if self.player_victory(PLAYER_1):
            return PLAYER_1
        return ""

    def get_neighbor(self, row, column, player):
        # I think the logic here is flawed, because we defo don't get all neighbors. 
        if player == PLAYER_1:
            board = self.transposed_board
        else:
            board = self.board
        row_edge = len(board)
        column_edge = len(board[row_edge - 1]) 
        neigh = []
        def add_valid_node(node):
            if node.is_valid(player):
                node.visit()
                neigh.append(node_information)
        # Row neighbors:
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
        return neigh
        
    def player_victory(self, player):
        if player == PLAYER_2:
            board = self.board
        else:
            board = self.transposed_board
        row_edge = len(board) - 1
        first_line = board[0]
        queue = [node_info(node, 0 ,i) for i, node in enumerate(first_line) if node.value == player]
        while queue:
            first_of_the_queue = queue[0]
            row, column = first_of_the_queue.row, first_of_the_queue.column 
            board[row][column].visit()
            if row == row_edge:
                return True
            queue = queue[1:] # Dequeue
            next_nodes = self.get_neighbor(row, column, player)
            queue += next_nodes
        return False

    def transpose_board(self):
        board = deepcopy(self.raw_board)
        transpose = []
        split_board = board.split('\n')
        l = [re.sub('\s', '', line) for line in split_board]
        spaces_to_add = 0
        end_spaces = len(split_board) -1
        for line in zip(*l):
            padding = list(map(lambda x: Node('.'), range(spaces_to_add)))
            padding += list(Node(val) for val in line)
            padding += list(map(lambda x: Node('.'), range(end_spaces)))
            transpose.append(padding)
            spaces_to_add += 1
            end_spaces -= 1
        self.transposed_board = transpose 
    # My theoretical solution requires a queue, as if this is a graph:
    # We start from an initial node, then add it to the queue.
    # The algorithm works as follows: Dequeue from the queue.
    # The dequed node has neighbors (from that player and also not visited).
    # Enqueue them, rinse and repeat. 
    # The algorithm declares victory if it finds a node in the winning edge.
    # If the queue ends before it, that player did not win.
    # Problems with this: defining neighboring because of the shape: Any space between \n and X,O or . is the tabbing...
    # Processing the board as a graph
    # Defining nodes properly so we know when they were visited. 