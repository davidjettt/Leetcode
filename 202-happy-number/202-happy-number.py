class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()

        
        while n not in visited:
            if n == 1:
                return True
            
            visited.add(n)
            n = self.sumOfSquares(n)
            # arr = [ int(i) for i in str(n) ]
            

#             for num in arr:
#                 res = 0
#                 res += num**2
            
#             n = res
            
        return False
                
            
    
    def sumOfSquares(self, n:int) -> bool:
        
        res = 0
        
        while n:
            digit = n % 10
            digit = digit ** 2
            res += digit
            n = n // 10
            
        return res
            