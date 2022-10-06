class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        dec1 = self.binarytoDecimal(a)
        dec2 = self.binarytoDecimal(b)
        
        return bin(dec1 + dec2).replace('0b', '')
    
    
    def binarytoDecimal(self, s):
        
        return int(s, 2)
        
#         decimal, n, i = 0, 0, 0
        
#         while s != 0:
#             dec = s % 10
            
#             decimal = decimal + dec * pow(2, i)
            
#             s = s // 10
            
#             i += 1
#         return s
            
        