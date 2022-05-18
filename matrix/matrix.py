from operator import methodcaller
class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix = list(map(methodcaller("split", " "), matrix_string.split('\n')))
    def row(self, index):
        
                    
        return list(map(int, self.matrix[index-1]))
        
    def column(self, index):
        matrix = self.matrix
        column = [row[index-1] for row in matrix]
        return list(map(int, column))
