class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
         0           5
        [1,0,-1,0,-2,2]
         a b  c d
         
           0.              5
         [-2, -1, 0, 0, 1, 2 ]
           i.     j.    l  r 
        
        -2, 0, 1, 1
        -2 + -1 + 0 + 2 = -1
        
        [2,2,2,2,2] t = 8
             i j l r
         
         [1] t = 1
        
        
        using double for loop to get first 2 values
            
            using 2 pointers to compute the last 2 values
            
            compare our curSum with target
                if curSum > target: move right pointer
                if curSum < target: move left pointer
                if curSum == target: add values to result, move left pointer until lands on new number (possibly for more quadruplets)
            
            
            return res
            
            [0,0,0,0]
             i j l r
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
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             for j in range(i + 1, n - 3):
#                 if j > i + 1 and nums[j] == nums[j - 1]:
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
        
        
        
        