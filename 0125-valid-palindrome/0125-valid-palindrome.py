class Solution:
    def isPalindrome(self, s: str) -> bool:
#         word = ''.join(x for x in s if x.isalnum()).lower()
#         if word == word[::-1]:
#             return True
#         else:
#             return False
        
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
            

        return True