class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # needs to be Time O(n) Space O(1)
        # length of nums will always be odd
        # every num appears twice execpt for one
        
        # what i know
            # need to look at every single num once to determine if there is a duplicate
            
#         n = len(nums)    
#         r = nums[0]
        
#         for i in range(1, n):
#             r = r ^ nums[i]
            
#         return r
        
        res = 0
        
        for n in nums:
            res = res ^ n
            
        return res
#         count = {}
        
#         for n in nums:
#             if n not in count:
#                 count[n] = 1
#             else:
#                 count[n] += 1
                
        
#         for k,v in count.items():
#             if v == 1:
#                 return k