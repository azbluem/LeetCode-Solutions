class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        for row_ind in range(len(matrix)):
            for item_ind in range(len(matrix[row_ind])):
                if matrix[row_ind][item_ind] == 0:
                    rows.add(row_ind)
                    columns.add(item_ind)
        for row in range(len(matrix)):
            for item in range(len(matrix[0])):
                if row in rows or item in columns:
                    matrix[row][item] = 0
                    