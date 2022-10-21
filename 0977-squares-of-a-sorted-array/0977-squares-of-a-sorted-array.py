class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Time O(nlogn)
        # Space O(n)
        
#         res = [ x**2 for x in nums ]
        
#         res.sort()
        
#         return res
        
        res = [''] * len(nums)
        
        resP = len(nums) - 1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                res[resP] = nums[left] ** 2
                resP -= 1
                left += 1
            else:
                res[resP] = nums[right] ** 2
                resP -= 1
                right -= 1
        
        # res[resP] = nums[left]
        return res
            
        
            
        
                
#     def sort(self, array):
#         less = []
#         equal = []
#         greater = []

#         if len(array) > 1:
#             pivot = array[0]
#             for x in array:
#                 if x < pivot:
#                     less.append(x)
#                 elif x == pivot:
#                     equal.append(x)
#                 elif x > pivot:
#                     greater.append(x)
#             # Don't forget to return something!
#             return self.sort(less)+equal+ self.sort(greater)  # Just use the + operator to join lists
#         # Note that you want equal ^^^^^ not pivot
#         else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
#             return array
                
            
 
        