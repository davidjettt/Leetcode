class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = sum(nums[:3])
        
        for i in range(len(nums) - 2):
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                
                if abs(threeSum - target) < abs(res - target):
                    res = threeSum
                    
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    return threeSum
        
        return res