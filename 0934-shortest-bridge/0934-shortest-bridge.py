class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """"
        
        [
            [ 0, 1 ],
            [ 1, 0 ]
        ]
        [
            [ 0, 1, 0 ],
            [ 0, 0, 0 ],
            [ 0, 0, 1 ]
        ]
        
        [
            [ 1, 1, 1 ,1 ,1 ],
            [ 1, 0, 0, 0, 1 ],
            [ 1 ,0, 1, 0, 1 ],
            [ 1, 0, 0, 0, 1 ],
            [ 1, 1, 1, 1, 1 ]
        ]
            
        """
        
        visited = set()
        dims = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def out_of_bounds(r, c):
            return r < 0 or c < 0 or r == dims or c == dims
        
        def dfs(r, c):
            if out_of_bounds(r, c) or grid[r][c] == 0 or (r, c) in visited:
                return

            visited.add((r, c))
            for dirX, dirY in directions:
                dfs(r + dirX, c + dirY)
        
        def bfs():
            res = 0
            q = collections.deque(visited)
            while q:
                qLength = len(q)
                for i in range(qLength):
                    row, col = q.popleft()
                
                    for dirX, dirY in directions:
                        newX, newY = dirX + row, dirY + col
                        if out_of_bounds(newX, newY) or (newX, newY) in visited:
                            continue
                        if grid[newX][newY] == 1:
                            return res
                        q.append((newX, newY))
                        visited.add((newX, newY))
                res += 1
                
        for r in range(dims):
            for c in range(dims):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()
        

    
                                
                                
                                
                                
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    