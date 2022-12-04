class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        '''
        
        [
            [2,0,0,1],
            [0,3,1,0],
            [0,5,2,0],
            [4,0,0,2]
        ]
        
        [
            [5,7,0],
            [0,3,1],
            [0,5,0]
        ]
        
        
        check diagonals for non zeros (if find 0 return false), can do same logic for even and odd length grids
        also mark positions as visited
        
        check all other cells for zeros (if find non zero return false)
        
        '''
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if r == c or (r + c) == n - 1:
                    if grid[r][c] == 0:
                        return False
                elif grid[r][c] != 0:
                    return False
        return True
        
        
        # Time O(n * m) where n is size of rows and m is size of cols
        # Space O(n) where n is size of set
#         visited = set()
        
#         r, c = 0, 0
#         # primary diagonal
#         while r < len(grid) and c < len(grid):
#             if (r, c) not in visited:
#                 visited.add((r, c))
#                 if grid[r][c] == 0:
#                     return False
            
#             r += 1
#             c += 1
            
#         # secondary diagonal
#         r, c = 0, len(grid) - 1
#         while r < len(grid) and c >= 0:
#             if (r, c) not in visited:
#                 visited.add((r, c))
#                 if grid[r][c] == 0:
#                     return False
            
#             r += 1
#             c -= 1
        
#         for r in range(len(grid)):
#             for c in range(len(grid)):
#                 if (r, c) not in visited and grid[r][c] != 0:
#                     return False
#         return True
        