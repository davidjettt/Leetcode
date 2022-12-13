class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        '''
        # Time O(n)
        # Space O(n)
        freq_map = {}
        buckets = [[] for _ in range(len(s) + 1)]
        
        for char in s:
            freq_map[char] = 1 + freq_map.get(char, 0)

        for char, count in freq_map.items():
            buckets[count].append(char)

        res = []
        for i in range(len(buckets) - 1, -1, -1):
            for char in buckets[i]:
                # res += (char * i)
                res.append(char * i)
        return ''.join(res)
        
        
        
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



            


