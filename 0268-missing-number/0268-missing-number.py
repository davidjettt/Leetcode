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

#         nums.sort()
#         for i in range(len(nums)):
#             if i != nums[i]:
#                 return i
            
#         return len(nums)
    
        sum1 = sum(nums)
        sum2 = 0
        
        for i in range(len(nums) + 1):
            sum2 += i
            
            
        return sum2 - sum1
    
    
        
    
        
        # return (len(nums) * (len(nums) + 1)) // 2 - sum(nums)

        