class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        # put the string in a set
        # if the length of the set is 26 then return true
        
        
        letters = set()
        
        for c in sentence:
            letters.add(c)
            
        if len(letters) == 26:
            return True
        else:
            return False
        