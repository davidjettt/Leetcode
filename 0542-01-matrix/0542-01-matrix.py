
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        visited = set()
        from collections import deque
        q = deque()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    visited.add((i,j))
                    q.append((i,j))
        
        while q:
            x,y = q.popleft()
            for dirr in [(1,0), (-1,0), (0,1), (0,-1)]:
                newX, newY = x+dirr[0], y+dirr[1]
                if newX >= 0 and newX <= len(matrix)-1 and newY >= 0 and newY <= len(matrix[0])-1 and (newX, newY) not in visited:
                        matrix[newX][newY] = matrix[x][y] + 1
                        visited.add((newX, newY))
                        q.append((newX, newY))
        return matrix

#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         """
#         need to check every single cell
#         if a cell is 0, then output for that cell is 0
#         if a cell is 1, then output for that cell is the nearest 0 (can only go up-down-left-right)
#         [
#             [0, 0, 0],
#             [0, 1, 0],
#             [1, 1, 1]
#         ]
#         use bfs algo
#         init result array 
#         put first value in queue
#         while there is still stuff in queue
#             pop off from front of queue
#             if that value is a 0 then do nothing 
#             else 
#         """
#         rows = len(mat)
#         cols = len(mat[0])
        
        
#         def bfs(r, c):
#             q = collections.deque()
#             q.append(((r, c), 0))
#             visited = set()
            
#             while q:
#                 coord, distance = q.popleft()
#                 row, col = coord
#                 if coord == 1:
#                     mat[row][col] = distance
#                     return
#                 # visited.add((r, c))
                
#                 directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#                 for dx, dy in directions:
#                     new_row = row + dx
#                     new_col = col + dy
                    
#                     if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
#                         q.append(((new_row, new_col), distance + 1))
#                         visited.add((new_row, new_col))
                        
                
                
            
#         for r in range(rows):
#             for c in range(cols):
#                 if mat[r][c] == 1:
#                     bfs(r, c)
                    
#         return mat
                    
#         row = len(mat)
#         col = len(mat[0])
#         q = deque()
        
#         for i in range(row):
#             for j in range(col):
#                 if mat[i][j] == 0:
#                     q.append((i, j))
                    
        
        # res = []
        # visited = set()
        # one = None
        # q = deque()
        # deque.append([0, 0])
        
#         for row in range(len(mat)):
#             for col in range(len(mat[0])):
#                 if mat[row][col] == 1:
#                     one = [row, col]
#                     neighbors = self.getNeighbors(mat, row, col)
                    
#                     for neighbor in neighbors:
#                         q.append(neighbor)
                        
#                     count = 0
#                     while len(q):
#                         curr = q.popleft()

#                         if mat[curr[0]][curr[1]] == 0:
#                             count += 1
#                             mat[one[0]][one[1]] = count
#                             q = deque()
#                         else:
#                             count += 1
                      
            
        