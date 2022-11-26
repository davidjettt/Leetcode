class Solution:
    def longestPalindrome(self, s: str) -> str:
        """"
        b a b a d
        
        a n n a x y z
        l     r
        
      
         loop through the input string
         
         each iteration check for odd and even length substrings
         
         checking if the letters of right and left 
            if they are the same, compare the length of it with our result
        
        
        for odd, left, right pointers start at the same place
        for even, right pointer starts at left + 1
        
        return result
         Time O(n^2)
         Space O(1)
        """
        
        res = ''
        res_len = 0
        
        for i in range(len(s)):
            # odd
            
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                
                l -= 1
                r += 1
            
            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r- l + 1 > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                
                l -= 1
                r += 1
        
        return res
        
        
        # BRUTE FORCE APPROACH
#         res = 'a'
#         for i in range(len(s)):
#             for j in range(i, len(s) + 1):
#                 # print(s[i:j])
#                 if s[i:j] == s[i:j][::-1]:
#                     if len(s[i:j]) > len(res): 
#                         res = s[i:j]
                        
#         return res
        
        