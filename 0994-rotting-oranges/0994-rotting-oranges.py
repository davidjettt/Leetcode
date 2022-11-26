import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        
        [
            [2,1,1],
            [1,1,1],
            [0,1,2]
        ]
        
        [
            [2,2,2],
            [2,2,0],
            [0,2,2]
        ]
        
        
        [
            [2,1,1],
            [0,1,1],
            [1,0,1]
        ]
        
        
        iterate through the grid
        run bfs on every 2 we find
        
        bfs
            pop off from queue
            * might need to do something here *
            check for neighbors that are 1s
            before add neighbors to queue, increment our result by 1
            add to our visited set
            
        1) have a check for 1s in first loop (like an else if) 
        2) after done w/ bfs, loop through grid again looking for 1s
        '''
        # Time O(n * m)
        # Space O(n + m)
        res = [0] # 1
        rows, cols = len(grid), len(grid[0])
        visited = set() 
        q = collections.deque() # [  (2,2, 4)  ]
        fresh_oranges = [0]
        
        def bfs():
            while q:
                r, c, mins = q.popleft()  # (2,1,3)
                
                if grid[r][c] == 1:
                    grid[r][c] = 2
                
                
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dirX, dirY in directions:
                    newX, newY = dirX + r, dirY + c
                    
                    if 0 <= newX < rows and 0 <= newY < cols and (newX, newY) not in visited and grid[newX][newY] == 1:
                        fresh_oranges[0] -= 1
                        visited.add((newX, newY))
                        q.append((newX, newY, mins + 1))
                if len(q) == 0:
                    res[0] = mins
            
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 and (r, c) not in visited:
                    q.append((r, c, 0))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges[0] += 1
                    
        bfs()
        return -1 if fresh_oranges[0] > 0 else res[0]
        
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             return -1
        # return res[0]        
        
        