class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # log3 (3) = 27
        
        num = 3 
        
        if n == 0:
            return False
        if n == 1:
            return True
        
        while num <= n:     
            if num != n:
                num *= 3   
                print(num)
            else:
                break
                
        return num == n   