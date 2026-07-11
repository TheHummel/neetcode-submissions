class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search row:
        l = 0
        r = len(matrix) -1
        mid = (r-l) // 2
        row = None

        if len(matrix) == 1:
            row = 0

        if target < matrix[0][-1]:
            if target < matrix[0][0]:
                return False
            else:
                row = 0
        elif target > matrix[-1][-1]:
            return False

        while l<r and row is None:
            mid = l + (r-l) // 2
            print(l, mid, r, r-l <= 1)
            x = matrix[mid][-1]
            if r-l <= 1:
                if target <= matrix[l][-1]:
                    row = l
                else:
                    row = r
            elif x == target:
                return True
            elif x < target:
                l = mid
            else:
                r = mid

        l = 0
        print("Entering row", row)
        r = len(matrix[row])-1

        if len(matrix[row]) == 1:
            print("a")
            return target == matrix[row][0]

        if target < matrix[row][0] or target > matrix[row][-1]:
            print("b")
            return False

        while l < r:
            mid = l + (r-l) // 2
            x = matrix[row][mid]
            print(l, mid, r, x)
            if x == target:
                return True
            if r - l <= 1:
                return target == matrix[row][l] or target == matrix[row][r]
            if x < target:
                l = mid
            else:
                r = mid


        return False
        