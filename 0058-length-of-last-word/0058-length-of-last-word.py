class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        
        
        s2 = s.strip()
        
        s_list = s2.split(' ')
        
    
        return len(s_list[-1])
        