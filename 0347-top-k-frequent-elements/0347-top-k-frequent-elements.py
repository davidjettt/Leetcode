class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        [ 1, 1, 1, 2, 2, 3 ]  k = 2
                  
             {
                1: 3,
                2: 2,
                3: 1
             }     
             
             [(1, 3), (2, 2), (3, 1)]
                              
                              
        [ 1, 1, 1, 1, 1, 1, 1, 1, 2 ] k = 1 [1]
        
        [(1, 8),(2, 1) ]
           i
        
                  
        1 2 3
        1, 2
        
        [ 1, 2 ]
        
        make a frequency map  n
        
        sort the hashmap based on value  nlogn
            sorted(hashamp.items(), reversed, key=lambda x:x[1])
            
        iterate through sorted list k times and appending element to result n 
        
        Time O(nlogn) where n is the size of the nums array
        Space O(n + m) where n is size of the sorted array, and m is size of hashmap
        '''
        
        res = [] # [1, 2]
        frequency_map = {}
        
        for n in nums:
            frequency_map[n] = 1 + frequency_map.get(n, 0)
            
        
        sorted_list = sorted(frequency_map.items(), key=lambda x:x[1])
        
        for i in range(len(sorted_list) - 1, -1, -1):
            if k == 0:
                break
            else:
                res.append(sorted_list[i][0])
                k -= 1
            
        return res