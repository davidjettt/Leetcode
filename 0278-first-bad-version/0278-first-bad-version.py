# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # Time O(logn) where n is number of versions
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
        
#         l, r = 1, n
        
#         while l < r:
        
#             mid = (l + r) // 2
            
#             if isBadVersion(mid) == True:
#                 r = mid
        
#             # if not bad then need to go to the right
#             else:
#                 l = mid + 1
                
#         return l