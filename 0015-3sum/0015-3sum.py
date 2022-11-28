class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        
        '''
        # Time O(n2)
        # Space O(n)
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
        
        
        
        