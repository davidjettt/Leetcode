class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        [ 100, 4, 200, 1, 3, 2 ] output: 4
            
        1 2 3 4
        
        [100, 4, 200, 1, 3, 2]
        
        res = 4
        [ 1, 2, 3, 4, 100, 200 ]
                            l    r
        
        
        
        [ 0, 1, 10, 9, 4, 5, 2 ]  3
        
        0 1 2
        
        4 5
        
        9 10
        
        [-1, -10, -5, 0, -3, -2 ] 4
        
        -3 -2 -1 0
        
        res = 2
        [1,3, 5, 6]
              l  r
        
        res= 3
        [ 1, 3, 6, 7, 10, 11, 12 ] 3
                       l       r
        
        '''
        
        
        unique = list(set(nums))
        
        unique.sort()
        
        if len(unique) == 1:
            return 1
        if len(unique) == 0:
            return 0
        
        l, r = 0, 1
        
        res = 1
        
        while r < len(unique):
            if unique[r] - 1 == unique[r - 1]:
                res = max(res, r - l + 1)
                
            else:
                l = r
            
            r += 1
            
        return res
        
        
        