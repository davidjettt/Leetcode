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
              l   r
        
        
        
        
        
        '''
        
        
        
        
        l, r = 0, len(s1) - 1
        chars = {}
        for c in s1:
            chars[c] = 1 + chars.get(c, 0)
        
        while r < len(s2):
            chars2 = {}
            
            for i in range(l, r + 1):
                chars2[s2[i]] = 1 + chars2.get(s2[i], 0)
                
            if chars2 == chars:
                return True
            # if sorted(s1) == sorted(s2[l:r+1]):
            #     return True
            
            l += 1
            r += 1
        
        return False
            