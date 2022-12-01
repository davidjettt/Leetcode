class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        
        while matrix:
            # pop off the first row
            row = matrix.pop(0)
            # concatanate that row to the result
            res.extend(row)
            # # rotate matrix counter clock wise by creating tuples with zip method and then reversing it
            matrix = [*zip(*matrix)][::-1]
            
        return res
