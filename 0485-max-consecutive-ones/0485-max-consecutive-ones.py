class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        
        max_ones = 3
        curr = 3
        [ 1, 1, 0, 1, 1, 1 ]
                            
        
        [ 1, 0, 0, 1, 1, 1, 0 ]
                               i
        
        '''
        # Time O(n) where n is the size of the nums array
        # Space O(1)
        max_ones = 0 # 3
        curr = 0 # 0
        
        for n in nums:
            if n == 1:
                curr += 1
            else:
                max_ones = max(max_ones, curr)
                curr = 0
        
        
        return curr if curr > max_ones else max_ones
        