class Solution:
    @staticmethod
    def generate_matrix(n: int) -> list[list[int]]:
        """

        Coordinate order:
        [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [1, 1]]

        Example:
        Solution.generateMatrix(9)
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]

        """

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        value = 1
        while top <= bottom and left <= right:
            for column in range(left, right + 1):
                matrix[top][column] = value
                value += 1
            top += 1
            for row in range(top, bottom + 1):
                matrix[row][right] = value
                value += 1
            right -= 1
            if top <= bottom:
                for column in range(right, left - 1, -1):
                    matrix[bottom][column] = value
                    value += 1
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = value
                    value += 1
                left += 1
        return matrix

    @staticmethod
    def gen_matrix_recursive(n: int):
        if n == 0:
            return []

        if n == 1:
            return [[1]]
