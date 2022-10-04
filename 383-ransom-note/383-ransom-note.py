class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        chars_bank = []
        
        # iterate through magazine and store each character in list
        # iterate through ransomNote and check if character is in list
        # if true then remove character from list
        # return false if character isn't in list
        # if able to iterate through entire string then return false
        
        
        chars_bank = [ char for char in magazine ]
        
        
        for char in ransomNote:
            
            if char in chars_bank:
                chars_bank.remove(char)
            else:
                return False
        
        return True
            
        
        
        