# class Solution:
#     def findMedian(self, matrix):
#         arr = []
#         for i in matrix:
#             arr.extend(i)
        
#         arr.sort()

#         print(arr)

#         if len(arr) % 2 == 0:
#             num1 = arr[len(arr)//2]
#             num2 = arr[len(arr)//2-1]

#             print(num1 + num2 / 2)
        
#         else:
#             print(arr[len(arr)//2])

class Solution:
    def findElementsLesserThanMid(self, target: int, row: list):
        lo = 0
        hi = len(row)

        while lo < hi:
            mid = (lo + hi) // 2

            if row[mid] < target:
                lo = mid +1
            else:
                hi = mid
            
        return lo

    def findMedian(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        length = (n*m)
        lo = min([row[0] for row in matrix])
        hi = max([row[-1] for row in matrix])
        desired = length // 2

        while lo < hi:
            mid = (lo + hi) // 2
            count = 0

            for row in matrix:
                count += self.findElementsLesserThanMid(mid, row)

            if count < desired:
                lo = mid + 1
            else:
                hi = mid
        return lo


a = Solution()
print(a.findMedian([ [1, 4, 9], [2, 5, 6], [3, 7, 8] ]))