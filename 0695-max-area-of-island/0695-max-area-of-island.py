class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # bfs / dfs
        # init visited set, max_area var, stack
        # loop though each value of the matrix
        # if encounter a 1 and that node hasn't been visited yet, add to stack and visited set (will add tuple to stack of node and current area count)
        # init current area count somewhere
        # pop from stack and increment current area count each time
        # check for valid neighbors of the node and add those to set and stack
        # keep repeating until stack is empty
        # once stack is empty get the max between current area and max area
        # find more islands
        
        
        if not grid:
            return 0
        
        visited = set()
        max_area = 0
        
        stack = collections.deque()
        
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and grid[r][c] not in visited:
                    curr_area = 0
                    stack.append((r, c))
                    visited.add((r, c))
                    
                    while len(stack) > 0:
                        row, col = stack.popleft()
                        
                        curr_area += 1
                        
                        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        
                        for dirX, dirY in directions:
                            newX, newY = row + dirX, col + dirY
                            
                            if 0 <= newX < rows and 0 <= newY < cols and (newX, newY) not in visited and grid[newX][newY] == 1:
                                stack.append((newX, newY))
                                visited.add((newX, newY))
                    
                    max_area = max(max_area, curr_area)
                    
        return max_area
                        