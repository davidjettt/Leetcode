class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        
        while matrix:
            
            row = matrix.pop(0)
            
            res.extend(row)
            
            matrix = [*zip(*matrix)][::-1]
            
        return res
