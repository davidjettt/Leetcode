class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        mid, low, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            
            if nums[mid] == 2:
                temp = nums[high]
                nums[high] = nums[mid]
                nums[mid] = temp
                
                high -= 1
            
            elif nums[mid] == 0:
                temp = nums[low]
                nums[low] = nums[mid]
                nums[mid] = temp
                
                low += 1
                mid += 1
            
            else:
                mid += 1
                