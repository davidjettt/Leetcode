class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        
        'cat'
        
        'tac'
        
        'ab' considered a permutation of 'ab' ?
        
        1) is the substring length == length of s1
        2) do the letters of substring match letters of s1
        
        
        {
            'a': 1,
            'b': 1
        }
                
        
        e i d b a o o o
          l r
        
        
        
        
        
        '''
        # Time O(n * m) where n is the length of s2 and m is the length of s1
        # Space O(n * m) where n is the size of chars and m is the size of chars2
        if len(s1) > len(s2): return False
        
        l, r = 0, len(s1) - 1
        s1_chars = {}
        s2_chars = {}
        
        for i in range(len(s1)):
            s1_chars[s1[i]] = 1 + s1_chars.get(s1[i], 0)
            s2_chars[s2[i]] = 1 + s2_chars.get(s2[i], 0)
            
        while r < len(s2):
            if s2_chars == s1_chars:
                return True
            
            if s2_chars[s2[l]] == 1: 
                s2_chars.pop(s2[l])
            else:
                s2_chars[s2[l]] -= 1
            
            l += 1
            r += 1
            if r < len(s2):
                s2_chars[s2[r]] = 1 + s2_chars.get(s2[r], 0)
        return False
            
        
        
#         while r < len(s2):
#             chars2 = {}
#             for i in range(l, r + 1):
#                 chars2[s2[i]] = 1 + chars2.get(s2[i], 0) 
#             if chars2 == s1_chars:
#                 return True
#             l += 1
#             r += 1
        
#         return False
            