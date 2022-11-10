class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        midpoint = len(nums) // 2
        
        left_arr = self.sortArray(nums[:midpoint])
        right_arr = self.sortArray(nums[midpoint:])
        
        return self.merge(left_arr, right_arr)
        
    
    
    def merge(self, left, right):
        res = []

        left_i, right_i = 0, 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] <= right[right_i]:
                res.append(left[left_i])
                left_i += 1
            else:
                res.append(right[right_i])
                right_i += 1

        res.extend(left[left_i:])
        res.extend(right[right_i:])

        return res