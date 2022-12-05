class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        '''
        res = 15
        {2, 9}
        curSum = 0
        
        [1,5,4,2,9,9,9] k = 3
         l   r
        
        {4}
        currSum = 8
        [4, 4, 4, 1, 2, 3] k = 3
        lr
        
        curSum = 0
        {4, 1}
        [4,4,1]
         l.  r
        
        set initial window pos and set
        
        iterate through the nums arr
            check if length of set matches k
            if true, compare currSum with res
            if false, update curSum and set before moving window
        
        
        return res
        
        [1,1,1,7,8,9]
         l. r
        
        '''
        res = 0
        curr_sum = 0
        l = 0
        seen = set()
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            while nums[r] in seen or r - l + 1 > k:
                seen.remove(nums[l])
                curr_sum -= nums[l]
                
                l += 1
            seen.add(nums[r])
            
            if r -l + 1 == k:
                res = max(res, curr_sum)
        
        return res
        
        
        
        
        # Time O(n * k) where n is the size of nums array and k is size of window
        # Space O(n)
        res = 0
        
        l, r = 0, k - 1
        
        while r < len(nums):
            curr_sum = 0
            distinct = set()
            
            for i in range(l, r + 1):
                if nums[i] in distinct:
                    curr_sum = 0
                    break
                
                distinct.add(nums[i])
                curr_sum += nums[i]
            
            res = max(curr_sum, res)
            
            l += 1
            r += 1
        
        return res
                