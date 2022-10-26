class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # Time O(nlogn) + O(nlogn)
        # Space O(n + m) 
        
#         s_sort = sorted(s)
#         t_sort = sorted(t)
        
#         return True if s_sort == t_sort else False
    
        # Time O(2n) -> O(n)
        # Space O(n)
        letters = {}
    
        for char in s:
            letters[char] = 1 + letters.get(char, 0)
            
        
        for char in t:
            if char not in letters:
                return False
            
            else:
                if letters[char] == 1:
                    del letters[char]
                else:
                    letters[char] -= 1
        
        return len(letters) == 0