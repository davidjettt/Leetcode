class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Time O(nlogn)
        # Space O(1)
        
#         missingNum = 0 
#         nums.sort()

#         for n in nums:
#             if n == missingNum:
#                 missingNum += 1
#             else:
#                 return missingNum
#         return missingNum
    
        
        return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)

        