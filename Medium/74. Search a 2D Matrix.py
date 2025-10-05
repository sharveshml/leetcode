class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix)-1, len(matrix[0])-1

        while n>=0 and m>=0:
            if matrix[n][m] == target:
                return True
            elif n > 0 and target <= matrix[n-1][m]:
                n = n-1
            else:
                m = m-1
        return False