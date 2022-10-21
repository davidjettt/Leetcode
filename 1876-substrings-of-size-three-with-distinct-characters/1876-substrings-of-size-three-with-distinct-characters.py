class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        # init two pointers windowStart = 0, windowEnd = 2
        # init count variable
        
        # use while loop as long as windowEnd < len(s)
            
            # init chars = empty set
            # put s[windowStart], s[windowEnd], s[windowStart + 1] in the set
            
            # if length of set is not 3 then add windowStart++ and windowEnd++ and then move on to next iteration/substring
            # else count++
            
        
        # return count
        
        # Time O(n) where n is the number of chars in the string
        # Space O(1) worst case scenario the set will only have a max of 3 chars in it
        
        if len(s) < 3:
            return 0
        
        windowStart = 0
        windowEnd = 2
        count = 0
        
        while windowEnd < len(s):
            chars = set()
            
            chars.update([ s[windowStart], s[windowStart + 1], s[windowEnd] ])
            # chars.add(s[windowStart])
            # chars.add(s[windowStart + 1])
            # chars.add(s[windowEnd])
            
            if len(chars) == 3:
                count += 1
            
            windowStart += 1
            windowEnd += 1
                
        return count