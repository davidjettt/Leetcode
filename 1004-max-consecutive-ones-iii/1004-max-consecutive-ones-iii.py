class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        
        {
            1: 0,
            0: 1
        }
        [1,1,1,0,0,0,1,1,1,1,0]  k = 2
                   l           r
        
        [0,0,1,1,1,0,0] k=0
        
        
        iterate through the array
            add value to frequency map
            
            check if nums[0] > k
                if true, then remove number left pointer points to from hashmap and  move left pointer
                keep doing this until nums[0] == k
                
            if nums[0] <= k, then we have valid sequence so check window length and compare with result
            
            
        
        return res 
        
        
        Time O(n) where n is the size of the input array
        Spaec O(1) 
        
        '''
        res = 0 
        curr_seq = 0
        count = {1: 0, 0: 0}
        l = 0
        
        if k == 0:
            for i in range(len(nums)):
                if nums[i] == 1:
                    curr_seq += 1
                    res = max(res, curr_seq)
                else:
                    curr_seq = 0
            return res
        
        for r in range(len(nums)):
            count[nums[r]] += 1
            
            while count[0] > k and l < r:
                count[nums[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res
        
        