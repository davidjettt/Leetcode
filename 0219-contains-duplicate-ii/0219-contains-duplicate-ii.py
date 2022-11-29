class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        
        [ 1, 2, 3, 1 ]
                   i
                   
        [ 1, 0, 1, 1 ]
                   i
    
        {
          1: 0
        }
         0   1. 2. 3. 4. 5
        [ 1, 2, 3, 1, 2, 3 ] k = 2
          i                 
        
        iterate through the array
        
        check if number is in hashmap
            check if abs(i - j) <= k
            if true, return true
            if false, replace old idx with new idx in hashmap
        
        storing num and index as key: value pair
        
        return true
        
        Time O(n)
        Space O(n)
        '''
        
        unique = {}
        
        for i in range(len(nums)):
            if nums[i] in unique:
                if abs(i - unique[nums[i]]) <= k:
                    return True
                else:
                    unique[nums[i]] = i
            
            else:
                unique[nums[i]] = i
    
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
    
        # hashmap = {}

#         for idx, val in enumerate(nums):
#             if val in hashmap and abs(idx - hashmap[val]) <= k:
#                 return True

#             hashmap[val] = idx
#         return False

                    
        
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