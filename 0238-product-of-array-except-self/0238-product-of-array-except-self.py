class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,3,4]
           
        [1,1,2,6]
        
        [24,12,4,1]
        
        [4,3,2,1]
        
        [1,4,12,24]
    
        
        make right and left arrays 
        compute right and left arrays
        reverse the right array
        mult the same indicies and assign that to the idx of our answer array
        
        [1,1,2,6]
 
        '''
        
        
        # Time O(n)
        # Space O(1)
#         length = len(nums)
#         answer = [1] * length
#         prefix, postfix = 1, 1
        
#         for i in range(length):
#             answer[i] = prefix
#             prefix *= nums[i]

#         for i in range(length - 1, -1, -1):
#             answer[i] *= postfix
#             postfix *= nums[i]
        
#         return answer
        
    
        # Time O(n)
        # Space O(n)
        n = len(nums)
        answer = [] 
        left, right = [1] * n, [1] * n
        nums_reversed = nums[::-1]
        
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1] 
        
        
        for i in range(1, n):
            right[i] = right[i - 1] * nums_reversed[i - 1]
            
        right_reversed = right[::-1]
        for i in range(n):
            answer.append(left[i] * right_reversed[i])
        
        return answer
    
    

        
#         length = len(nums)
#         answer = [''] * length
#         prefix, postfix = [], []
#         curr_product, curr_product2 = 1, 1

#         for i in range(length):
#             curr_product *= nums[i]
#             prefix.append(curr_product)
        
#         for i in range(length - 1, -1, -1):
#             curr_product2 *= nums[i]
#             postfix.append(curr_product2)
            
        
#         answer[0] = 1 * postfix[::-1][1]
#         answer[-1] = prefix[-2] * 1
        
#         for i in range(1, length - 1):
#             prefix_val = prefix[i - 1]
#             postfix_val = postfix[::-1][i + 1]
            
#             answer[i] = prefix_val * postfix_val
    
#         return answer


#         # Time O(n^2)
#         # Space O(1)
#         answer = [''] * len(nums)        
#         for i in range(len(answer)):
#             curr_product = 1
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 else:
#                     curr_product *= nums[j]
#             answer[i] = curr_product
#         return answer