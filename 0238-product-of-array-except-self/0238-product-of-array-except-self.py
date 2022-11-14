class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [''] * length
        pre, post = 1, 1
        
        for i in range(length):
            answer[i] = pre
            pre *= nums[i]
        print(answer)
        for i in range(length - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]
        
        
        
        return answer
        
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
            
#         postfix.reverse()
        
#         answer[0] = 1 * postfix[1]
#         answer[-1] = prefix[-2] * 1
        
#         for i in range(1, length - 1):
#             prefix_val = prefix[i - 1]
#             postfix_val = postfix[i + 1]
            
#             answer[i] = prefix_val * postfix_val
    
#         return answer
        
        # answer = [''] * len(nums)        
        # for i in range(len(answer)):
        #     curr_product = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         else:
        #             curr_product *= nums[j]
        #     answer[i] = curr_product
        # return answer