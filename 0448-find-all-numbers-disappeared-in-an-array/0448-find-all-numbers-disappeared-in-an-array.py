class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # The range is [1, length of the array]
        # Need to return an array with numbers that are not within that range
        
        # Time O(n)
        # Space O(1)
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
            
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
                
        return res
        
        # Time O(n)
        # Space O(n)
#         range_nums = set()
        
#         for num in range(1, len(nums) + 1):
#             range_nums.add(num)
            
#         # print(range_nums)
        
#         for num in nums:
#             if num in range_nums:
#                 range_nums.remove(num)
                
#         return list(range_nums)
            

        
    
    
        