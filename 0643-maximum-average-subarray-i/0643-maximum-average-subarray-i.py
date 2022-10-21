class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
#           0  1   2   3   4   5
#         [ 1, 12, -5, -6, 50, 3 ]
#           s           e

        windowStart = 0
        windowSum = 0
        maxAvg = float('-inf')
        
        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            
            if windowEnd >= k - 1:
                maxAvg = max(maxAvg, windowSum / k)
            
                windowSum -= nums[windowStart]
                windowStart += 1
        
        return maxAvg
            
        
#         windowStart = 0
#         windowEnd = k - 1
#         maxAvg = float('-inf')
        
#         if len(nums) == 1:
#             return nums[0]
        
#         while windowEnd < len(nums):
#             subArrSum = 0
            
#             for i in range(windowStart, windowEnd + 1):
#                 subArrSum += nums[i]
#             maxAvg = max(maxAvg, subArrSum / k)
            
#             windowStart += 1
#             windowEnd += 1
        
#         return maxAvg

        
        

            
        
        
        