class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        '''
                                 
        
        
        nums.sort()
        res, quad = [], []
        
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return
            
            l, r = start, len(nums) - 1
            while l < r:
                two_sum = nums[l] + nums[r]
                if two_sum > target:
                    r -= 1
                elif two_sum < target:
                    l += 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        kSum(4, 0, target)
        return res
               
        
#         res = []
#         n = len(nums)
        
#         if n < 4:
#             return res
        
#         nums.sort()
        
#         for i in range(n - 3):
#             # if i > 0 and nums[i] == nums[i - 1]:
#             #     continue
#             for j in range(i + 1, n - 3):
#                 if j > i + 1 and nums[i] == nums[j]:
#                     continue
#                 l, r = j + 1, n - 1
                
#                 while l < r:
#                     curr_sum = nums[i] + nums[j] + nums[l] + nums[r]
#                     if curr_sum > target:
#                         r -= 1
#                     elif curr_sum < target:
#                         l += 1
#                     else:
#                         res.append([nums[i], nums[j], nums[l], nums[r]])
#                         l += 1
#                         while nums[l] == nums[l - 1] and l < r:
#                             l += 1
        
#         return res
        
        
        
        