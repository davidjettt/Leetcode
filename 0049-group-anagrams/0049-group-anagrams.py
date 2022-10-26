class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        # res = {}
        
        for s in strs:
            count = [0] * 26   # a.....z  index 0 is a; index 25 is z
            
            for c in s:
                # ascii value of current char - ascii value of 'a' gives correct index of char in count 
                count[ord(c) - ord('a')] += 1
            
            # need to change to a tuple bc python doesn't allow lists to be values of dictionary
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
    
    
    
   