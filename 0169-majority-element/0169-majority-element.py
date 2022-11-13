class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for key, val in count.items():
            if val > len(nums) // 2:
                return key
        
        
        
        
        
        
        
        # Time O(2n) Space O(n)
#         counts = {}
        
#         for num in nums:
#             if num not in counts:
#                 counts[num] = 1
#             else:
#                 counts[num] += 1
        
#         res = 0
#         majority = 0
        
#         for num in counts:
#             if counts[num] > majority:
#                 majority = counts[num]
#                 res = num
#         return res

#         count = {}
#         res, max_count = 0, 0
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)
#             res = num if count[num] > max_count else res
#             max_count = max(max_count, count[num])
            
#         return res
    
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
        
            
        

            