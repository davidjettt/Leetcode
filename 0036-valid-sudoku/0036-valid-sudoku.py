import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
         {
            0: set(),
         }
        
        {
            (0 , 1 ):
        }
        
        
        iterate through the entire board
            check if value at the current cell already exists in hashmaps
            
                if true, return false
            
            add that value to the hashsets
        
        return true
        
        Time O(9^2)
        Space O(n)
        
        '''
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue
                if value in rows[r] or value in cols[c] or value in squares[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                squares[(r // 3, c // 3)].add(value)
        
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
