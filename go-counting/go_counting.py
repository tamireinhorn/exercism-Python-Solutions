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
        self._board_height = len(board) -1
        self._board_width = len(board[0]) -1
        self._black_territories = []
        self._white_territories = []

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
        if y < 0 or x < 0 or y > self._board_height or x > self._board_width:
            raise ValueError("Invalid coordinate")
        board = self.board
        examined_terr = board[y][x]
        neighbors = self.get_neighbors(x, y)
        return None, {}

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        pass
    
    def get_neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        """Find all the neighboring territories of a defined coordinate.

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            list[tuple[int, int]]: List of tuples defining (column, row) on the board for the territories neighboring the specified one.
        """
        neighbors = []
        if x != self._board_width:
            neighbors.append((x+1, y))
        if x != 0:
            neighbors.append((x-1, y))
        if y != self._board_height:
            neighbors.append((x, y+1))
        if y != 0:
            neighbors.append((x, y-1))
        return neighbors
