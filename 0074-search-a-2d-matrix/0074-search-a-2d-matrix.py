class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time O(logm + logn) where m is the number of rows and n is the number of columns
        # Space O(1)
        low_row_idx, high_row_idx = 0, len(matrix) - 1
        
        while low_row_idx <= high_row_idx:
            mid_row_idx = (low_row_idx + high_row_idx) // 2
            
            if matrix[mid_row_idx][-1] < target:
                low_row_idx = mid_row_idx + 1
            elif matrix[mid_row_idx][0] > target:
                high_row_idx = mid_row_idx - 1
            else:
                break
                
                
        if low_row_idx > high_row_idx: 
            return False
        
        left, right = 0, len(matrix[0]) - 1
        new_row_idx = (low_row_idx + high_row_idx) // 2
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[new_row_idx][mid] < target:
                left = mid + 1
            elif matrix[new_row_idx][mid] > target:
                right = mid - 1
            else:
                return True
        
        return False