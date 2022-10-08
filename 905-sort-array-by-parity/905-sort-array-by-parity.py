class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        # Time O(2n)   Space O(n)
        
        
#         if len(nums) == 1:
#             return nums
        
#         res = []
        
#         for n in nums:
#             if n % 2 == 0:
#                 res.append(n)
                
        
#         for n in nums:
#             if n % 2 != 0:
#                 res.append(n)
                
                
#         return res

        if len(nums) == 1:
            return nums

        l, r = 0, len(nums) - 1
    
        while l < r:
            
            if nums[l] % 2 != 0 and nums[r] % 2 == 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                
                l = l + 1
                r = r - 1
            elif nums[l] % 2 == 0 and nums[r] % 2 == 0:
                    l = l + 1
            elif nums[l] % 2 != 0 and nums[r] % 2 != 0:
                r = r - 1
            else:
                l = l + 1
                r = r - 1
        
        return nums