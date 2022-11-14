class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars_bank = {}
        
        for char in magazine:
            chars_bank[char] = 1 + chars_bank.get(char, 0)
        
        for char in ransomNote:
            if char in chars_bank:
                if chars_bank[char] == 0:
                    return False
                else:
                    chars_bank[char] -= 1
            else:
                return False
        return True
            
            
        
        
        # Time O(n + m) where n is the size ransomNote and m is size of magazine
        
        # Space O(n) where n is size of chars_bank