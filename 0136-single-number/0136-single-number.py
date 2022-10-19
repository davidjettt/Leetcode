class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # needs to be Time O(n) Space O(1)
        
        
        count = {}
        
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
                
        
        for k,v in count.items():
            if v == 1:
                return k
            