class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        # res = {}
        
        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
            
        return res.values()

#     def isAnagram(self, string1, string2): 
#         letters = {}
    
#         for char in string1:
#             letters[char] = 1 + letters.get(char, 0)
            
        
#         for char in string2:
#             if char not in letters:
#                 return False
            
#             else:
#                 if letters[char] == 1:
#                     del letters[char]
#                 else:
#                     letters[char] -= 1
        
#         return len(letters) == 0
    
    
    
   