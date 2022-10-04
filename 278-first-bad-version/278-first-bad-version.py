# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # [ 1, 2, 3, 4, 5 ]
        # binary search
        
        l, r = 1, n
        
        while l < r:
        
            mid = (l + r) // 2
            
            if isBadVersion(mid) == True:
                r = mid
        
            # if not bad then need to go to the right
            else:
                l = mid + 1
                
        return l
        
        
        # Time O(logn)
        # Space O(1)