class Solution:
    def frequencySort(self, s: str) -> str:
        '''

        can make three bucket sort arrays and iterate through all three of them at the same time to form new string

        first need to make a frequency map
        make bucket sort array (length of arr will be 62 b/c lower and capital letters and digits)
            where idx represents number of times letter appears


        tree

        123Aaabc      aa123Abc


        []
        '''
        # Time O(nlogn)
        # Space O(n)
#         freq_map = {}
#         for char in s:
#             freq_map[char] = 1 + freq_map.get(char, 0)
        
#         x = sorted(freq_map.items(), key=lambda x:x[1], reverse=True)  
        
#         res = ''
#         for char, count in x:
#             res += (char * count)
        
#         return res
        
        
        
        
        freq_map = {}
        lowercase = [[] for _ in range(len(s) + 1)]
        uppercase = [[] for _ in range(len(s) + 1)]
        digits = [[] for _ in range(len(s) + 1)]

        for char in s:
            freq_map[char] = 1 + freq_map.get(char, 0)

        for char, count in freq_map.items():
            if char.isnumeric():
                digits[count].append(char)
            elif char.isupper():
                uppercase[count].append(char)
            else:
                lowercase[count].append(char)
        
        i = len(s)
        res = ''
        while i >= 0:
            for x in lowercase[i]:
                res += (x * i)
            for y in uppercase[i]:
                res += (y * i)
            for z in digits[i]:
                res += (z * i)
            i -= 1
        return res
            


