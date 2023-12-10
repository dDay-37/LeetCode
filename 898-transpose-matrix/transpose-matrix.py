class Solution(object):
    def transpose(self, matrix):
        mat = [ [0 for y in range(len(matrix))] for y in range(len(matrix[0]))] 
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                mat[col][row] = matrix[row][col]
        return mat


        