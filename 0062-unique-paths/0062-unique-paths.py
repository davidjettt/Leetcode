class Solution:
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        '''
        '''
        # Time O(m * n) where m is row size and n is col size
        # Space O(m + n)
        if f"{m},{n}" in memo:
            return memo[f"{m},{n}"]
        if m == 1 or n == 1:
            return 1
        
        unique_path1 = self.uniquePaths(m - 1, n, memo)
        unique_path2 = self.uniquePaths(m, n - 1, memo)
        memo[f"{m},{n}"] = unique_path1 + unique_path2

        return memo[f"{m},{n}"]

        # row = [1] * n
        # for i in range(m - 1):
        #     new_row = [1] * n
        #     for j in range(n - 2, -1, -1): 
        #         new_row[j] = new_row[j + 1] + row[j]   
        #     row = new_row
        # return row[0]


