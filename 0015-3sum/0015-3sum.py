class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
                
            
            left, right = i + 1, len(nums) - 1    
            
            while left < right:
                totalSum = nums[i] + nums[left] + nums[right]
                
                if totalSum > 0:
                    right -= 1
                elif totalSum < 0:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        
            
        
        return triplets
                    
                    
        
        # Time O(nlogn) + O(n^2) = O(n^2)
        # Space O(n) because of the built in sort method
        
        
        
        