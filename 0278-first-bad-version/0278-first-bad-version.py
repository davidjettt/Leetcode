# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # 1, 2, 3, 4, 5
        #        r  lm 
        
        
        # initilize left & right pointers, result variable
        # performing binary search between version 1 - n
        # calculate the midpoint
        # run api call on the midpint
        # if api call returns true, update our result variable and move right pointer
        # if api call returns false, move left pointer
        
        # once binary search ends (when left > right), return result variable
        
        # Time O(logn)
        # Space O(1)
        
        first_bad = 0
        l, r = 1, n 
        
        while l <= r:
            version = (l + r) // 2 
            
            if isBadVersion(version) == True:
                first_bad = version
                r = version - 1
            else:
                l = version + 1
                
        return first_bad
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # [ 1, 2, 3, 4, 5 ]
        # binary search
        
#         l, r = 1, n
        
#         while l < r:
        
#             mid = (l + r) // 2
            
#             if isBadVersion(mid) == True:
#                 r = mid
        
#             # if not bad then need to go to the right
#             else:
#                 l = mid + 1
                
#         return l
        
        
        # Time O(logn)
        # Space O(1)