class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        [1] -> [1] [0] -> false

        [9,2,1,3,5] -> [9,1] [2,3,5] -> true

        [2, 9, 7]        [2,7] [9] -> true

        '''
        # Time O(n * sum(nums))
        # Space O(sum(nums))
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) / 2
        dp = set()
        dp.add(0)
        for i in range(len(nums)):
            next_dp = set()
            for t in dp:
                if target in dp:
                    return True
                next_dp.add(t + nums[i])
                next_dp.add(t)
            dp = next_dp

        return False

        # Time O(n * sum(nums))
        # Space (n * sum(nums)) because of the keys in memo
        if sum(nums) % 2 == 1: 
            return False

        target = sum(nums) / 2
        memo = {}
        def dfs(target, i):
            if (target, i) in memo:
                return memo[(target, i)]
            if target == 0:
                return True
            if target < 0:
                return False
            
            if i + 1 < len(nums):
                if dfs(target - nums[i + 1], i + 1):
                    return True
                if dfs(target, i + 1):
                    return True
            memo[(target, i)] = False
            return False

        return dfs(target - nums[0], 0) or dfs(target, 0)


        # target = sum(nums) / 2
        # memo = {}
        # def dfs(num, i):
        #     if (num, i) in memo:
        #         return memo[(num, i)]
        #     if num > target:
        #         return False
        #     if num == target:
        #         return True


        #     if i + 1 < len(nums):
        #         if dfs(num + nums[i + 1], i + 1):
        #             return True
        #         if dfs(num, i + 1):
        #             return True
            
        #     memo[(num, i)] = False
        #     return False

        # return dfs(nums[0], 0) or dfs(0, 0)
