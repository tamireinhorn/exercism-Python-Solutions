class Queen:
    def __init__(self, row: int, column: int) -> None:
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row 
        self.column = column

    def can_attack(self, another_queen) -> bool:
        same_row = another_queen.row == self.row
        same_column = another_queen.column == self.column
        if same_column and same_row:
            raise ValueError("Invalid queen position: both queens in the same square")
        diagonal = abs(self.row - another_queen.row) == abs(self.column - another_queen.column)
        return same_column or same_row or diagonal
