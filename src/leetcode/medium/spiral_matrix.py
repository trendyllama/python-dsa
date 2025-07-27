from typing import List


class Solution:
    @staticmethod
    def generateMatrix(n: int) -> List[List[int]]:
        """

        Coordinate order:
        [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [1, 1]]

        Example:
        Solution.generateMatrix(9)
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]

        """

        final_num = n**2

        main_matrix: List[List[int | None]] = [
            [None for _ in range(n)] for _ in range(n)
        ]

        incrementor = (i for i in range(1, final_num + 1))

        coordinate_pairs = []

        for i, row in enumerate(main_matrix):
            for j, col in enumerate(row):
                match (i, j):
                    case (0, _):
                        main_matrix[i][j] = next(incrementor)
                    case (_, n):
                        main_matrix[j][i] = next(incrementor)

            # want to swap the indexes

    @staticmethod
    def gen_matrix_recursive(n: int):
        if n == 0:
            return []

        if n == 1:
            return [[1]]
