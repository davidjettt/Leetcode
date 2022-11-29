class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        biggestMinHeight = 1 
        
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
        length of y-axis -> min(end2a[1], end2b[1]) min(v1, v2)
        
        1, 7  maxArea = 49
        y = 1
        x = r - l 8
        
        
        start pointers at end of arr
        
        calcaulate area for that container
        
        compare that area with our maxArea (get the bigger one)
        
        move the pointer that points to the smaller value
        
        what if both pointers point to same height? 
            move both pointers?
            
        return maxArea
        
        '''
        max_area = 0
        
        l, r = 0, len(height) - 1
        
        while l < r:
            x_axis = r - l
            y_axis = min(height[l], height[r])
            area = x_axis * y_axis
            
            max_area = max(max_area, area)
            
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_area
            
        