class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    count += 1
                    # print(visited)
                    visited.add((r, c))
                    q = deque()
                    q.append((r, c))
                    
                    while len(q) > 0:
                        curr = q.popleft()
                        # neighbors = self.getNeighbors(grid, curr[0], curr[1])
                        
                        if grid[curr[0]][curr[1]] == '0':
                            continue
                            
                        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                        for dir in dirs:
                            new_row, new_col = curr[0] + dir[0], curr[1] + dir[1]
                            # check if within bounds
                            if new_row >= 0 and new_row <= len(grid) - 1 and new_col >= 0 and new_col <= len(grid[0]) - 1:
                                if (new_row, new_col) not in visited:
                                    visited.add((new_row, new_col))
                                    q.append((new_row, new_col))
                        
                        # try:
                        #     neighbors = self.getNeighbors(grid, curr[0], curr[1])
                        # except IndexError:
                        #     continue 
#                         neighbors = getNeighbors(grid, curr[0], curr[1])
                    
#                         for neighbor in neighbors:
#                             if neighbor not in visited:
#                                 visited.add(neighbor)
#                                 stack.append([*neighbor])
        
        return count
                        
            
            
    
#         def getNeighbors(grid, row, col):
#             neighbors = []
#             dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#             for dir in dirs:
#                 new_row, new_col = row + dir[0], col + dir[1]
#                 # check if within bounds
#                 if new_row >= 0 and new_row <= len(grid) - 1 and new_col >= 0 and new_col <= len(grid[0]) - 1:
#                     if (new_row, new_col) not in visited:
#                         neigbors.append((new_row, new_col))
#             return neighbors
    
#     def getNeighbors(self, grid, row, col):
#         res = []
        
#         # Top
#         if row > 0 and grid[row - 1][col]:
#             res.append((row - 1, col))
#         # Bottom
#         if row < len(grid) - 1 and grid[row + 1][col]:
#             res.append((row + 1, col))
#         # Right
#         if grid[row][col + 1]:
#             res.append((row, col + 1))
#         # Left
#         if grid[row][col - 1]:
#             res.append((row, col - 1))
#         return res