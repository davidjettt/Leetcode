class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        {
            'r1': {5, 3, 7}
        }
        
        board[r][0]
        
        if c == 0:
            add num to col set
        
        
        if board[r][0]
        
        
        set up the hashmap 
        
        iterate through the board
        
        at each row position add num to hashmap for corresponding key value
        also check for duplicate
        
        same for cols
        
        0-2, 3-5, 6-8 for x and y
        
        
        
        '''
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': 
                    continue
                if board[r][c] in cols[c] or board[r][c] in rows[r] or board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c //3)].add(board[r][c])
                
        return True
        
#         rows = {
#             0: set(),
#             1: set(),
#             2: set(),
#             3: set(),
#             4: set(),
#             5: set(),
#             6: set(),
#             7: set(),
#             8: set()
#         }
#         columns = {
#             0: set(),
#             1: set(),
#             2: set(),
#             3: set(),
#             4: set(),
#             5: set(),
#             6: set(),
#             7: set(),
#             8: set()
#         }
#         i = -1
        
#         for r in range(9):
#             i += 1
#             if board[r][i] in columns[r]:
#                 return False
#             columns[r].add(board[r][i])
#             for c in range(9):
#                 if board[r][c] in rows[c]:
#                     return False
#                 rows[c].add(board[r][c])
                
        
#         return True