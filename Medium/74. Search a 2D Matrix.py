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

# Binary Search Approach
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n*m-1

        while left <= right:
            mid = left+(right-left) // 2
            num = matrix[mid // m][mid % m]

            if num == target:
                return True
            
            elif target < num:
                right = mid - 1

            else:
                left = mid+1
        return False

        