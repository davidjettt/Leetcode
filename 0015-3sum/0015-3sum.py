class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        [ -1, 0, 1, 2, -1, -4 ]
        
        [ [-1, 0, 1], [-1, -1, 2] ]
        
        
        res = [[-1, -1, 2], [-1, 1, 0]]
        
        [ -4, -1, -1, 0, 1, 2 ]
               i.        lr                    
          
          
        iterate through length of nums array - 2
        
            check of triplets already exist in result array
            
            left pointer start at i + 1
            right pointer start at end of array
            
            use while loop as long as left < right
            
            binary search based off of the total sum
            
            total sum > 0: move right pointer
            total sum < 0: move left pointer
            
            if find tatal sum == 0: check if it already exists in the result array
            
            
            return result at the end
        [ -1, 0, 0, 1]
          i      l  r
        
        [0, 0, 0]
         i.    lr
        
        '''
        
        triplets = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if nums[i] == nums[i - 1] and i > 0:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                total_sum = nums[i] + nums[l] + nums[r]
                
                if total_sum > 0:
                    r -= 1
                elif total_sum < 0:
                    l += 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:    
                        l += 1
                        
        
        return triplets
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         triplets = []
#         nums.sort()
        
        
#         for i in range(len(nums)):
#             # checks for duplicates
#             if i > 0 and nums[i - 1] == nums[i]:
#                 continue
                
            
#             left, right = i + 1, len(nums) - 1    
            
#             while left < right:
#                 totalSum = nums[i] + nums[left] + nums[right]
                
#                 if totalSum > 0:
#                     right -= 1
#                 elif totalSum < 0:
#                     left += 1
#                 else:
#                     triplets.append([nums[i], nums[left], nums[right]])
#                     left += 1
#                     # Checks for duplicates and if still in bounds
#                     while nums[left] == nums[left - 1] and left < right:
#                         left += 1
                        
            
        
#         return triplets
                    
                    
        
        # Time O(nlogn) + O(n^2) = O(n^2)
        # Space O(n) because of the built in sort method
        
        
        
        