class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
            [0, 1, 9, 16, 100]
              i       
            [-4,-1,0,3,10]
                   lr    
              
            [4, 4, 4, 9, 16]
              i      
            [-3, 2, 2, 2, 4]
                       lr   
            
            
            get the squares of the right and left pointers
            add the bigger value into the i pos of the answer array
            move i pointer and right or left pointer 
            once right and left pointers meet then add that last square to answer array
        '''
        res = [''] * len(nums)
        
        l, r = 0, len(nums) - 1
        i = len(nums) - 1
        
        while l <= r:
            left_square = nums[l] ** 2
            right_square = nums[r] ** 2
            
            if left_square < right_square:
                res[i] = right_square
                r -= 1
            else:
                res[i] = left_square
                l += 1
            i -= 1
            
        
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Time O(nlogn)
        # Space O(n)
        
#         res = [ x**2 for x in nums ]
        
#         res.sort()
        
#         return res
        
        # Time O(n)
        # Space O(n)
        res = [''] * len(nums)
        
        resP = len(nums) - 1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            leftSquare = nums[left]**2
            rightSquare = nums[right]**2
            if leftSquare > rightSquare:
                res[resP] = leftSquare
                left += 1
            else:
                res[resP] = rightSquare
                right -= 1
                
            resP -= 1
        
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
                
            
 
        