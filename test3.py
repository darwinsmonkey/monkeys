import numpy as np

matrix1 = np.array([[4, 2, 0, 0, 5, 4],
                    [2, 3, 1, 6, 1, 3],
                    [0, 0, 6, 0, 5, 8],
                    [3, 4, 0, 3, 1, 7],
                    [0, 0, 0, 0, 5, 0],
                    [3, 4, 0, 3, 1, 7]], float)

class matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.a = int

    def main(self):
        matrix_temp = np.zeros((len(self.matrix-1), len(self.matrix[0]-1)), float)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                matrix_temp += matrix[0][i] * ((-1) ** (i + j)) * self.row_col_del()
        return matrix_temp

    def row_col_del(self):
        self.matrix = np.delete(self.matrix, 0, 0)
        self.matrix = np.delete(self.matrix, 0, 1)


M1 = matrix(matrix1)
print(M1.main())