class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        temp = -12
        res = 24
        min = -12
        max = 24
        [-2, 3, -4]
                   i

        '''
        res = max(nums)
        curr_min, curr_max = 1, 1
        
        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1
                continue

            # want to store in temp variable b/c want to keep the value the same for both curr_max and curr_min
            temp = curr_max * n
            curr_max = max(temp, curr_min * n, n)
            curr_min = min(temp, curr_min * n, n)
            res = max(curr_max, res)
        return res


        # dp = [float('-inf')] * len(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] < 0 and curr_product < 0:

        #     curr_product *= nums[i]

        #     if curr_product < dp[i - 1]:
        #         curr_product = 1
        #         dp[i] = dp[i - 1]
        #     else:
        #         dp[i] = curr_product
        # print(dp)
        # return max(dp[-1], max(nums))


        # l, r = 0, 0
        # res = 0
        # curr_prod = 1
        # while r < len(nums):
        #     curr_prod *= nums[r]

        #     if curr_prod > res:
        #         res = curr_prod
        #         r += 1
        #     else:
        #         r += 1
        #         l = r
        #         curr_prod = 1
        # return res