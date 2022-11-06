class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        def bfs(r, c):
            visited.add((r, c))
            q = collections.deque()
            q.append((r, c))
            
            while len(q) > 0:
                curr = q.popleft()

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
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    count += 1
        
        return count
                        