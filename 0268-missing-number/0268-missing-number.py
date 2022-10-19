class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # if len(nums) == 1:
        #     if nums[0] == 1:
        #         return 0
        
        allNums = []
        
        for i in range(1, len(nums) + 1):
            allNums.append(i)
            
        
        for n in allNums:
            if n not in nums:
                return n
        
        return 0
            