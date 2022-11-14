class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time O(n)
        # Space O(1)
        length = len(nums)
        answer = [''] * length
        prefix, postfix = 1, 1
        
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(length - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        
        return answer
        
#         # Time O(n)
#         # Space O(n)
#         n = len(nums)
#         answer = []
#         prefix, postfix = [1] * n, [1] * n
#         for i in range(1, n):
#             prefix[i] = prefix[i - 1] * nums[i - 1]
        
#         for i in range(1, n):
#             postfix[i] = postfix[i - 1] * nums[::-1][i - 1]
#             print(postfix)
        
#         for i in range(n):
#             answer.append(prefix[i] * postfix[::-1][i])
            
#         return answer
        
#         length = len(nums)
#         answer = [''] * length
#         prefix = []
#         postfix = []
#         curr_product, curr_product2 = 1, 1

#         for n in nums:
#             curr_product *= n
#             prefix.append(curr_product)
        
#         for i in range(length - 1, -1, -1):
#             curr_product2 *= nums[i]
#             postfix.append(curr_product2)
            
#         postfix[::-1]
        
#         answer[0] = 1 * postfix[1]
#         answer[-1] = prefix[-2] * 1
        
#         for i in range(1, length - 1):
#             prefix_val = prefix[i - 1]
#             postfix_val = postfix[i + 1]
            
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