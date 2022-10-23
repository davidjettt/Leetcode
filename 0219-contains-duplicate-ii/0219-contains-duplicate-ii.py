class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # nums at the indicies need to be the same
        # absolute value of i - j needs to be less than or equal to k
        # indicies can't be the same
        
        # init windowStart = 0 windowEnd = 1
        
        # while windowEnd < len(nums)
            # if abs(windowStart - windowEnd) <= k
                # if nums[windowStart] == nums[windowEnd]
                    # return True
                # else windowEnd++
            
            # if abs(windowStart - windowEnd) > k
                # move windowStart plus 1
                
        
#         if len(nums) < 2:
#             return False
        
#         if k == 0:
#             return False
        
#         windowStart, windowEnd = 0, 1
        
#         while windowEnd < len(nums):
            
#             if abs(windowStart - windowEnd) <= k:
#                 if nums[windowStart] == nums[windowEnd]:
#                     return True
#                 else:
#                     windowEnd += 1
#             else:
#                 windowStart += 1
        
#         return False
        i=0
        j=0
        seen = set()
        while j<len(nums):
            if j-i>k:
                seen.remove(nums[i])
                i+=1
                
            if nums[j] not in seen:
                seen.add(nums[j])
            else: return True
                    
            j+=1    
        return False
    
    
#         hmap = {}
        
#         for i in range(len(nums)):
#             if nums[i] not in hmap:
#                 hmap[nums[i]] = i
#             else:
#                 if abs(i - nums[i]) <= k:
#                     return True
        
#         return False