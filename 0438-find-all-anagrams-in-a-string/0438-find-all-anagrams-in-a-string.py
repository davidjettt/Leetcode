class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window
        # store characters in p string in hashmap
        # length of sliding window will be length of p string
        # loop through s string
        # have inner loop that loops through substring
        # check each character of substring if it is in hashmap (might need to make copy of hashmap b/c mutating it)
        # if in hashmap remove char from hashmap and move on to next character
        # if not in hashmap then break from loop
        # if go through entire substring successfully, add left pointer to res array
        # right and left pointers will increment by 1 once inner loop ends
        if len(p) > len(s): return []
        p_chars, s_chars = {}, {}
        
        for i in range(len(p)):
            p_chars[p[i]] = 1 + p_chars.get(p[i], 0)
            s_chars[s[i]] = 1 + s_chars.get(s[i], 0)
            
        l, r = 1, len(p)
        res = [0] if s_chars == p_chars else []
        
        while r < len(s):
            if s_chars[s[l - 1]] == 1:
                del s_chars[s[l - 1]]
            else:
                s_chars[s[l - 1]] -= 1
            # s_chars[s[l - 1]] -= 1 if s_chars[s[l - 1]] == 1 else del s_chars[s[l - 1]]
            s_chars[s[r]] = 1 + s_chars.get(s[r], 0)
            if s_chars == p_chars:
                res.append(l)
            
            l += 1
            r += 1
    
#         while r < len(s):
#             chars_copy = chars.copy()
            
#             for i in range(l, r + 1):
#                 if s[i] in chars_copy:
#                     if chars_copy[s[i]] == 1:
#                         del chars_copy[s[i]]
#                     else:
#                         chars_copy[s[i]] -= 1
#                 else:
#                     break
                
#             if len(chars_copy) == 0:
#                 res.append(l)
            
#             l += 1
#             r += 1
        
        return res
                
            
        
        
        
        