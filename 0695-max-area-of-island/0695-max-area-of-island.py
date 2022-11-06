class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time O(n * m) where n is number of rows and m is number of columns
        # Space O(n)
#         if not grid:
#             return 0
    
#         visited = set()
#         max_area = 0
#         stack = []
#         rows, cols = len(grid), len(grid[0])
        
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == 1 and grid[r][c] not in visited:
#                     curr_area = 0
#                     stack.append((r, c))
#                     visited.add((r, c))
                    
#                     while len(stack) > 0:
#                         row, col = stack.pop()
#                         curr_area += 1
                        
#                         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        
#                         for dirX, dirY in directions:
#                             newX, newY = row + dirX, col + dirY
                            
#                             if 0 <= newX < rows and 0 <= newY < cols and (newX, newY) not in visited and grid[newX][newY] == 1:
#                                 stack.append((newX, newY))
#                                 visited.add((newX, newY))
                    
#                     max_area = max(max_area, curr_area)
                    
#         return max_area
        visited = set()
        max_area = 0
        stack = []
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            curr_area = 0
            stack.append((r, c))
            visited.add((r, c))

            while len(stack) > 0:
                row, col = stack.pop()
                curr_area += 1
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dirX, dirY in directions:
                    newX, newY = row + dirX, col + dirY
                    if 0 <= newX < rows and 0 <= newY < cols and (newX, newY) not in visited and grid[newX][newY] == 1:
                        stack.append((newX, newY))
                        visited.add((newX, newY))
            return curr_area
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and grid[r][c] not in visited:
                    curr_area = dfs(r, c)
                    max_area = max(max_area, curr_area)        
        return max_area