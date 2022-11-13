class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == majority:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                majority = nums[i]
                count = 0
        return majority
        
#         # Time O(n)
#         # Space O(n)
#         count = {}
        
#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
        
#         for key, val in count.items():
#             if val > len(nums) // 2:
#                 return key
        

    
        # Time O(n)
        # Space O(1)
#         count = 1
#         res = nums[0]
        
#         for i in range(1, len(nums)):
#             if nums[i] == res:
#                 count += 1
#             else:
#                 count -= 1
            
#             if count < 0:
#                 res = nums[i]
#                 count = 0
#         return res
            
#         res, count = 0, 0
#         for n in nums:
#             if count == 0:
#                 res = n
#             count += (1 if res == n else -1)
#         return res
        
            
        

            