class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        a b c
            lr
        
        
        a n n a x y y.    10 
        
        iterate through the input string
            check for odd palindomes
                l, r will start at same position
                loop will continue as long as pointers are in bounds and have a valid palindrome substring
                increment res + 1
            check for even palidromes
                r pointer will start l + 1
                
            Time O(n^2)
            Space O(1)
        '''
        
        res = 0 # 
        
        for i in range(len(s)):
            # odd
            l, r = i, i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                
                l -= 1
                r += 1
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                
                l-= 1
                r += 1
                
        return res
            