import collections
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        '''
        {1 , 2 , 3}
        
      cols  {
            0: set(), {1}
            1: set(), { 1, 2 , 3}
            2: set() {1, 2 ,3 }
            ...
        }
        
        rows =   
        
        iterate through the matrix and add values to cols and rows hashset
        
        iterate through cols and rows hashset and compare each val in dictionary with default hashset
        
        return false for the 1st unequal hashset
        
        return true if we iterate through everything w/ o returning false
            
        '''
        n = len(matrix)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        
        for r in range(n):
            for c in range(n):
                rows[r].add(matrix[r][c])
                cols[c].add(matrix[r][c])
                
        default = set([ i for i in range(1, n + 1) ])
        for hashset in rows.values():
            if default != hashset:
                return False
            
        for hashset in cols.values():
            if default != hashset:
                return False
            
        
        return True
            