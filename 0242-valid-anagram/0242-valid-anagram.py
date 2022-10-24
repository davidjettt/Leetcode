class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
#         s_sort = sorted(s)
#         t_sort = sorted(t)
        
#         return True if s_sort == t_sort else False
    
        hashmap = {}
        
        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        
        for c in t:
                
            if c in hashmap:
                hashmap[c] -= 1
            else:
                return False
            
            if hashmap[c] == 0:
                del hashmap[c]
        
        return len(hashmap) == 0