class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_sort = sorted(s)
        t_sort = sorted(t)
        
        return True if s_sort == t_sort else False
        