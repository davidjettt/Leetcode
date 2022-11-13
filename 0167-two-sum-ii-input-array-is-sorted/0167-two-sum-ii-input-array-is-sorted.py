class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l <= r:
            
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        
        
        
        
        
        
        
#         left, right = 0, len(numbers) - 1
        
#         while left < right:
#             curr_sum = numbers[left] + numbers[right]
            
#             if curr_sum == target:
#                 return [left + 1, right + 1]
            
#             if curr_sum > target:
#                 right -= 1
#             else:
#                 left += 1
                
            