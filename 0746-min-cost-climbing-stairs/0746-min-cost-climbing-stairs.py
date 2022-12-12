class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        reaching the top is going to cost[len(cost)]

         
        need to do dfs when start on idx 0 and idx 1

        can use memo
            {idxNum: min steps it takes to reach target}
        get the min cost of both searches

            base case is when current step is len(cost)
            base case #2 is when current step is over len(cost)

            add to current cost before going to next step


        return min cost btwn start point of idx 0 and idx 1

        '''
        # True DP solution
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2]) 
        return min(cost[0], cost[1])

        # Time O(n) where n is the size of input array
        # Space O(n)
        memo = {}
        def dfs(step):
            if step in memo:
                return memo[step]
            if step >= len(cost):
                return 0
            
            cur_cost = cost[step] + dfs(step + 1)
            cur_cost2 = cost[step] + dfs(step + 2)
            memo[step] = min(cur_cost, cur_cost2)

            return memo[step]

        # return min(dfs(0), dfs(1))
        dfs(0)
        return min(memo[0], memo[1]) 