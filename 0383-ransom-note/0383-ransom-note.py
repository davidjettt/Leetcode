class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
                
        # iterate through magazine and store each character in list
        # iterate through ransomNote and check if character is in list
        # if true then remove character from list
        # return false if character isn't in list
        # if able to iterate through entire string then return false
        
        
#         chars_bank = [ char for char in magazine ]
        
        
#         for char in ransomNote:
            
#             if char in chars_bank:
#                 chars_bank.remove(char)
#             else:
#                 return False
        
#         return True
    
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
            
            
        
        
        # Time O(2n^2) for each char in ransomNote we are performing .remove
        
        # Space O(n) where n is size of chars_bank