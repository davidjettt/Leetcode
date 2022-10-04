class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # Checks if image exists or if current pixel is already the same color 
        if image is None or image[sr][sc] == color:
            return image
        
        
        self.fill(image, sr, sc, image[sr][sc], color)
        
        
        return image
        
        
        
        
    def fill(self, image, r, c, pixel_to_change, color):
    
        # Checking if we go out of bounds or if current pixel we are on doesn't need to be changed
        if r < 0 or r > len(image) - 1 or c > len(image[0]) - 1 or c < 0 or image[r][c] != pixel_to_change:
            return
        
        image[r][c] = color
        
        # Down
        self.fill(image, r + 1, c, pixel_to_change, color)
        
        # Up
        self.fill(image, r - 1, c, pixel_to_change, color)
        
        # Left 
        self.fill(image, r, c - 1, pixel_to_change, color)
        
        # Right
        self.fill(image, r, c + 1, pixel_to_change, color)