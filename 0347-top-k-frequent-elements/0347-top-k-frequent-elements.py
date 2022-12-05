class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        
        [1,1,1,2,2,3]
        
        1 2
        bucketSort = [[], [3], [2], [1], [], []]
                                i
        
        create count hashmap
        populting bucketsort array
        
        iterating through the array backwards
            going through each subarray and append that value to result
            we will be doing that k times
        
        return res
        '''
        res = []
        freq = {}
        counts = [ [] for _ in range(len(nums) + 1) ]
        
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
        # print(freq)
        # print(counts)
        for num, c in freq.items():
            counts[c].append(num)
            
        
        print(counts)
        for i in range(len(counts) - 1, -1, -1):
            if counts[i] == []:
                continue
            for n in counts[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
    
    
        # Time O(n)
#         res = [] 
#         frequency_map = {}
        
#         for n in nums:
#             frequency_map[n] = 1 + frequency_map.get(n, 0)
        
#         counts = [''] * (len(nums) + 1)

#         for n in frequency_map:
#             if counts[frequency_map[n]] != '': 
#                 counts[frequency_map[n]].append(n)
#             else:
#                 counts[frequency_map[n]] = [n]
                
#         for i in range(len(counts) - 1, 0, -1):
#             for n in counts[i]:
#                 res.append(n)
#                 if len(res) == k:
#                     return res

        # Time (nlogn) where n is the size of the nums array
        # Space (n + m) where n is the size of the sored array, and m is size of hashmap
#         res = [] 
#         frequency_map = {}
#         for n in nums:
#             frequency_map[n] = 1 + frequency_map.get(n, 0)
            
#         sorted_list = sorted(frequency_map.items(), key=lambda x:x[1])
        
#         for i in range(len(sorted_list) - 1, -1, -1):
#             if k == 0:
#                 break
#             else:
#                 res.append(sorted_list[i][0])
#                 k -= 1
            
#         return res