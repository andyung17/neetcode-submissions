class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        mid_index = start + (end - start) // 2

        while start <= end:

            mid_index = start + (end - start) // 2

            mid_index_row = (mid_index) // (len(matrix[0]))
            mid_index_col = (mid_index) % (len(matrix[0]))

            mid_value = matrix[mid_index_row][mid_index_col]

            if mid_value == target:
                return True
            elif mid_value > target:
                end = mid_index - 1
            elif mid_value < target:
                start = mid_index + 1

        return False