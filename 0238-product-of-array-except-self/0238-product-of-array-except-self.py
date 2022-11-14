class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init result array with the same length of nums
        # init pointer var for result array starting at the beginning
        # init product variable
        # loop through input array
            # if i == j
                # continue with the next iteration (this will be the number that we are excluding)
            # else:
                # multiply the values to the product variable
        
        # once the loop is done, we have the product for that index so resassign answer[i] to be the product
        # reset product variable
        
        # increment the i pointer and do the loop again
        length = len(nums)
        answer = [''] * length
        prefix = []
        postfix = []
        curr_product, curr_product2 = 1, 1

        for n in nums:
            curr_product *= n
            prefix.append(curr_product)
        
        for i in range(length - 1, -1, -1):
            curr_product2 *= nums[i]
            postfix.append(curr_product2)
            
        postfix.reverse()
        
        answer[0] = 1 * postfix[1]
        answer[-1] = prefix[-2] * 1
        
        for i in range(1, length - 1):
            prefix_val = prefix[i - 1]
            postfix_val = postfix[i + 1]
            
            answer[i] = prefix_val * postfix_val
    
        return answer
        
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