class Solution:
    def climbStairs(self, n: int) -> int:
        '''
                             
            4                       
           /\              
          3  2                    
         /\  /\                  
         2 1 1 0                  
         /\ 
         1 0
        /
        0


        '''
        # DP Bottom-Up solution without extra memory b/c we can just shift the one and two variables
        # Time O(n)
        # Space O(1)
        # one, two = 1, 1
        # for _ in range(n - 1):
        #     tmp = one
        #     one = one + two
        #     two = tmp
        # return one

        # DFS Memoization 
        # Time O(n)
        # Space O(n)
        memo = {}

        def dfs(step):
            if step in memo:
                return memo[step]
            if step > n:
                return 0
            if step == n:
                return 1
            
            s1 = dfs(step + 1)
            # memo[step + 1] = s1
            s2 = dfs(step + 2)
            # memo[step + 2] = s2
            memo[step] = s1 + s2
            return s1 + s2
        
        return dfs(1) + dfs(2)
