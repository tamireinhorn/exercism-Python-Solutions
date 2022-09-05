BLACK = "B"
WHITE = "W"
NONE = ""

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self._black_territories = set()
        self._white_territories = set()
        self._none_territories = set()

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        board = self.board
        if y < 0 or x < 0 or y >= len(board) or x >= len(board[0]):
            raise ValueError("Invalid coordinate")
        examined_terr = board[y][x]
        neighbors = self.get_neighbors(x, y)
        # To be more precise an empty intersection is part of a player's territory
        # if all of its neighbors are either stones of that player or empty
        # intersections that are part of that player's territory.
        if all(self.board[neighbor[1]][neighbor[0]] == BLACK for neighbor in neighbors):
            self._black_territories.add((x, y))
            return BLACK, self._black_territories
        elif all(self.board[neighbor[1]][neighbor[0]] == WHITE for neighbor in neighbors):
            self._white_territories.add((x,y))
            return WHITE, self._white_territories
        if examined_terr == BLACK or examined_terr == WHITE:
            return NONE, set()
        # It's not a stone and not fully surrounded by stones of one player: then we are in for it.
        

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        for row, _ in enumerate(self.board):
            for column, _ in enumerate(self.board[row]):
                self.territory(row, column)
        return {BLACK: self._black_territories, WHITE: self._white_territories, NONE: self._none_territories}
    
    def get_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        """Find all the neighboring territories of a defined coordinate.

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            list[tuple[int, int]]: List of tuples defining (column, row) on the board for the territories neighboring the specified one.
        """
        neighbors = []
        if x != len(self.board[0]):
            neighbors.append((x+1, y))
        if x != 0:
            neighbors.append((x-1, y))
        if y != len(self.board):
            neighbors.append((x, y+1))
        if y != 0:
            neighbors.append((x, y-1))
        return neighbors
