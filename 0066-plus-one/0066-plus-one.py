class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        num_string = ''
        
        for n in digits:
            num_string += str(n)
            
        num = int(num_string) + 1
        
        
        res = []
        
        for x in str(num):
            res.append(int(x))
            
            
        return res