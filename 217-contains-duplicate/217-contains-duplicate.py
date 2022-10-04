class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         nums2 = set(nums)
        
#         if len(nums2) < len(nums):
#             return True
#         else:
#             return False



    
    
    
    
    
    
    
    
    
        unique = set()
        
        for num in nums:
            
            if num in unique:
                return True
            
            else:
                unique.add(num)
        
        return False
            
            