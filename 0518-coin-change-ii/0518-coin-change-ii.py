class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        need to return how many diff combos of coins can make amount

        2 2 1
        1 2 2
        '''
        # Initialize a list of zeros with a length of the target amount + 1
        dp = [0] * (amount + 1)

        # The number of ways to make up 0 dollars is 1
        dp[0] = 1

        # Iterate over the coins
        for coin in coins:
            # Iterate over the amounts from 1 to the target amount
            for i in range(1, amount + 1):
                # If the current coin is less than or equal to the current amount, we can use it to make up the amount
                if coin <= i:
                    # The number of ways to make up the current amount is equal to the number of ways to make up the
                    # remaining amount (i.e. the current amount minus the value of the current coin) plus the number of ways
                    # to make up the current amount without using the current coin
                    dp[i] = dp[i] + dp[i - coin]

        # Return the number of ways to make up the target amount
        return dp[amount]
        
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
