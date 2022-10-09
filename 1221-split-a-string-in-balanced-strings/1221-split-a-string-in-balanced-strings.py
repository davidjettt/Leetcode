class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        # Need to return max num of balanced substrings tht can be formed from s
        # initiate balance var and res variable
        # loop through string
        # if c is a L increment balance var by 1; otherwise  - 1
        
        balance = 0
        res = 0
        
        for c in s:
            if c == 'L':
                balance += 1
            else:
                balance -= 1
                
            if balance == 0:
                res += 1
        return res