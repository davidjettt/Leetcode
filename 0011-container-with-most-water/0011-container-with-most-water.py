class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
         0           4.          8
        [1, 8, 6, 2, 5, 4, 8, 3, 7 ]
            l              r   
               
               
        [ 1, 3, 5, 1, 2, 1 ]
          l              r
        
        endpoints represent length of line
        
        endpoint1: (0, 0)
        endpoint2: (0, 1)
        
        (1, 0), (1, 8)
        
        (8, 0), (8, 7)
        
        
        length of x-axis -> 8 - 1 = 7 (length of pointers -> r - l)
        length of y-axis -> min(v1, v2)

        start pointers at end of arr
        
        calcaulate area for that container
        
        compare that area with our maxArea (get the bigger one)
        
        move the pointer that points to the smaller value
        
        what if both pointers point to same height? 
            move both pointers?
            
        return maxArea
        
        '''
        # Time O(n) where n is the size of height array
        # Space O(1)
        max_area = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            x_axis_len = r - l
            y_axis_len = min(height[l], height[r])
            area = x_axis_len * y_axis_len
            
            max_area = max(max_area, area)
            
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_area
    
        # BRUTE FORCE
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res
            
        