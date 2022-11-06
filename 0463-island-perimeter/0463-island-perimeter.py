class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # [
        #     [0,1,0,0],
        #     [1,1,1,0],
        #     [0,1,0,0],
        #     [1,1,0,0]
        # ]
        # if the 1 is adjacent to a 0 or out of bounds that counts as 1 side
        # total amount of adjacent 0s and out of bounds is the total perimeter of 1 square
        # if current node is a 1, check its neighbors
        # if its neighbors is out of bounds or a 0 then add 1 to result perimeter
        # but only add neighbors that are 1s to q
        
        
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        # stack = []
        
        def dfs(r, c):
            # if 0 > r >= rows and 0 > c >= cols or grid[r][c] == 0:
            #     return 1
            if 0 > r or r >= rows or 0 > c or c >= cols or grid[r][c] == 0:
                return 1
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            perim = dfs(r, c + 1)
            perim += dfs(r, c - 1)
            perim += dfs(r + 1, c)
            perim += dfs(r - 1, c)
            
            return perim
            

    
#         def dfs(r, c):
#             res = 0
#             visited.add((r, c))
#             stack.append((r, c))
#             while stack:
#                 row, col = stack.pop()
                
#                 directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
#                 for dirX, dirY in directions:
#                     newX, newY = row + dirX, col + dirY

#                     if 0 <= newX < rows and 0 <= newY < cols and (newX, newY) not in visited and grid[newX][newY] == 1:
#                         visited.add((newX, newY))
#                         stack.append((newX, newY))
#                     else:
#                         res += 1
            
#             return res
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)
        