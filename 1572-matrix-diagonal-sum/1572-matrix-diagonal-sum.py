class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        '''
        
        
        mat[0][0]
        mat[r + 1][c + 1]   -> doing this n times
        
        primary diag -> 
        
        (0, 2)
        (1, 1)
        (2, 0)
        
        secondary diag -> c -= 1 , r += 1
        row starts at 0, ends at len(mat) - 1
        col starts at n - 1 (len(mat) - 1), ends at 0
        
        col -= 1
        row += 1
        
        (0, 3)
        (1, 2)
        (2, 1)
        (3, 0)
        
        [
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]
        ]

        calcluate the primary diag by using for loop n times
        
        calculate the secondary diag
        
        do a check for odd length mat when r == c (in sec diagonal)
            
        
        '''
        # Time O(n + m) where n is the primary diag and m is the secondary diag
        # Space O(1)
        
        if len(mat) == 1:
            return mat[0][0]
        
        primary = 0 
        for i in range(len(mat)):
            primary += mat[i][i]
            
        
        secondary = 0 
        r, c = 0, len(mat) - 1
        while r < len(mat) and c >= 0:
            if r == c and len(mat) % 2 != 0:
                r += 1
                c -= 1
            
            secondary += mat[r][c]
            
            r += 1
            c -= 1
            
        return primary + secondary
        
#         n = len(mat)
        
#         mid = n // 2
        
#         summation = 0
        
#         for i in range(n):
            
#             # primary diagonal
#             summation += mat[i][i]
            
#             # secondary diagonal
#             summation += mat[n-1-i][i]
            
            
#         if n % 2 == 1:
#             # remove center element (repeated) on odd side-length case
#             summation -= mat[mid][mid]
            
            
#         return summation
        
        
        
