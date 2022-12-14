class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        need to return how many diff combos of coins can make amount

        2 2 1
        1 2 2
        '''
        
        memo = {}

        def dfs(i, a):
            if (i, a) in memo:
                return memo[(i, a)]
            if a == 0:
                return 1
            if a < 0:
                return 0
            if i == len(coins):
                return 0

            memo[(i, a)] = dfs(i, a - coins[i]) + dfs(i + 1, a)
            return memo[(i, a)]
        
        return dfs(0, amount)
