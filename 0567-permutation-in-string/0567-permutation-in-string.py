class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
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
        # Time O(26n) where n is size of s2 and 26 is the alphabet
        # Space O(n) where n is size of s2
        if len(s1) > len(s2): return False
        
        l, r = 0, len(s1) - 1
        s1_chars = {}
        s2_chars = {}
        
        for i in range(len(s1)):
            s1_chars[s1[i]] = 1 + s1_chars.get(s1[i], 0)
            s2_chars[s2[i]] = 1 + s2_chars.get(s2[i], 0)
            
        while r < len(s2):
            if s2_chars == s1_chars:   # This is O(26) operation, because worst case dict will be size 26
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
        
        
#         # NEETCODE SOLUTION Time O(n)
#         if len(s1) > len(s2): return False
        
#         s1_count, s2_count = [0] * 26, [0] * 26
#         for i in range(len(s1)):
#             s1_count[ord(s1[i]) - ord('a')] += 1
#             s2_count[ord(s2[i]) - ord('a')] += 1
            
#         matches = 0
#         for i in range(26):
#             matches += 1 if s1_count[i] == s2_count[i] else 0
            
#         l = 0
#         for r in range(len(s1), len(s2)):
#             if matches == 26: return True
            
#             index = ord(s2[r]) - ord('a')
#             s2_count[index] += 1
#             if s1_count[index] == s2_count[index]:
#                 matches += 1
#             elif s1_count[index] + 1 == s2_count[index]:
#                 matches -= 1
                
#             index = ord(s2[l]) - ord('a')
#             s2_count[index] -= 1
#             if s1_count[index] == s2_count[index]:
#                 matches += 1
#             elif s1_count[index] - 1 == s2_count[index]:
#                 matches -= 1
            
#             l += 1
#         return matches == 26
        
        # Time O(n * m) where n is the length of s2 and m is the length of s1
        # Space O(n * m) where n is the size of chars and m is the size of chars2
#         l, r = 0, len(s1) - 1
#         chars = {}
        
#         for c in s1:
#             chars[c] = 1 + chars.get(c, 0)
        
#         while r < len(s2):
#             chars2 = {}
#             for i in range(l, r + 1):
#                 chars2[s2[i]] = 1 + chars2.get(s2[i], 0) 
#             if chars2 == s1_chars:
#                 return True
#             l += 1
#             r += 1
        
#         return False
            