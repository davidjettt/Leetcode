class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        store nums array in hashset
        iterate though nums 
            check if n - 1 exists in set
            
            if false, count up to see if n + 1 exists in set (also keep track of length of seq), repeat until no more seq
            
            once we finish seq count, compare length with res 
            
            if true, do nothing
            
            
        return res
        '''
        # Time O(n) where n is the size of the set
        # Space O(n) where n is the size of the set
        res = 0
        nums_set = set(nums)
        
        for n in nums_set:
            if n - 1 not in nums_set:
                count = 1
                while n + count in nums_set:
                    count += 1
                
                res = max(res, count)
                
        return res

        # Time O(nlogn) where n is the size of the unqiue array
        # Space O(n) where n is the size of the set
#         unique = list(set(nums))
        
#         unique.sort()
        
#         if len(unique) == 1:
#             return 1
#         if len(unique) == 0:
#             return 0
        
#         l, r = 0, 1
#         res = 1
        
#         while r < len(unique):
#             if unique[r] - 1 == unique[r - 1]:
#                 res = max(res, r - l + 1)
#             else:
#                 l = r
#             r += 1
            
#         return res
        
        
        