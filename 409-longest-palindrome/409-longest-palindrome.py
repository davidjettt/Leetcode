class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if len(s) == 1:
            return 1
    
        letters = {}

        for c in s:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1
                
        res = 0
        odd = 0
                
        
        for count in letters.values():
            if count % 2 == 0:
                res += count
            else:
                res += count - 1
                odd += 1
                
        if odd > 0:
            res += 1
                
        return res
                

    
#         abccccdd

#         racecar
        
#         rrcaaec
        
#         {
#             'r': 2,
#             'a': 2,
#             'c': 2,
#             'e': 1
#         }
        
#         {
#             'a': 1,
#             'b': 1,
#             'c': 4,
#             'd': 2
#         }
        