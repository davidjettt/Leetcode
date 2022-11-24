class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # [
        #     [0,1,0,0],
        #     [1,1,1,0],
        #     [0,1,0,0],
        #     [1,1,0,0]
        # ]
        
        # iterate though grid until find a 1
        # do dfs on that 1
            # return 0 if already visited node
            # return 1 if node is out of bounds or a 0
            
            # calculate node's neighbors
            # do dfs on each neighbor
            # add to perimeter on each dfs return call
        
        # return dfs when it is finished
        
        # Time O(n * m)
        # Space O(n * m)
        rows, cols = len(grid), len(grid[0])
        visited = set() 
    
        def dfs(r, c):
            if (r, c) in visited:
                return 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 1
            
            visited.add((r, c))
            
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            perimeter = 0 # 16
            for dirX, dirY in directions:
                newX, newY = dirX + r, dirY + c
                perimeter += dfs(newX, newY)
            
            return perimeter
                
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
    
    
        
        # Time O(n * m) only visited each postion in the grid once
        # Space O(n * m) have visit set and recursive calls
#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         def dfs(r, c):
#             if 0 > r or r >= rows or 0 > c or c >= cols or grid[r][c] == 0:
#                 return 1
#             if (r, c) in visited:
#                 return 0
            
#             visited.add((r, c))
#             perim = dfs(r, c + 1)
#             perim += dfs(r, c - 1)
#             perim += dfs(r + 1, c)
#             perim += dfs(r - 1, c)
            
#             return perim
            
        
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1:
#                     return dfs(r, c)
        