class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''

        [1,1,2,3,1,1,1]

        [0,1,3]
        [0,1,0,3,2,3]
         i     j 

        3
        [3,3,2,1]
        [1,0,2,3]
         i     j   

        '''
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        print(dp)
        return max(dp)


        memo = {}
        res = [0]

        def dfs(subseq, i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                memo[str(subseq)] = len(subseq)
                return len(subseq)
            
            if nums[i] < subseq[-1]:
                subseq.append(nums[i])
                dfs(subseq, i + 1)
                memo[i] = len(subseq)
            else:
                memo[str(subseq)] = len(subseq)
                return len(subseq)

        

        for i in range(len(nums)):
            dfs([nums[i]], i + 1)
        return res[0]
        