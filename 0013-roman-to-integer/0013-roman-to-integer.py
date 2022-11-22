class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        
#         res = 0

#         prev = 0
#         for i in range(len(s) - 1, -1, -1):
#             symbol = s[i]
#             if roman[symbol] >= roman[s[prev]]:
#                 res += roman[symbol]
#             else:
#                 res -= roman[symbol]
        
#             prev = i
#         return res
    
    
        result = 0
        prev = 0
        
        for c in reversed(s):
            if roman[c] >= prev:
                result += roman[c]
            else:
                result -= roman[c]
            prev = roman[c]
            
        return result
        
        
#         for i in range(len(s)):
#             if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
#                 res -= roman[s[i]]
#             else:
#                 res += roman[s[i]]
                
#         return res
            