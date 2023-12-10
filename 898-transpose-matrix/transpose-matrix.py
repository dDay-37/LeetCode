class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(matrix)
        c = len(matrix[0])
        m = []
        for i in range(c):
            row = []
            for j in range(r):
                row.append(matrix[j][i])
            m.append(row)
        return m