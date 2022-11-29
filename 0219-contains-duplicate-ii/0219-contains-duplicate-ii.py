class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    
#         i, j = 0, 0
#         seen = set()
        
#         while j < len(nums):
#             if abs(i - j) > k:
#                 seen.remove(nums[i])
#                 i += 1
            
#             if nums[j] not in seen:
#                 seen.add(nums[j])
#             else:
#                 return True
#             j += 1
#         return False
    
        hashmap = {}

        for idx, val in enumerate(nums):
            if val in hashmap and abs(idx - hashmap[val]) <= k:
                return True

            hashmap[val] = idx
        return False

                    
        
#         if len(nums) < 2:
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