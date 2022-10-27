class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # Checks if image exists or if current pixel is already the same color 
        if image is None or image[sr][sc] == color:
            return image
        
        self.fill(image, sr, sc, image[sr][sc], color)
        return image
        
        
    def fill(self, image, r, c, initial_pixel, color):
        # Checking if we go out of bounds or if current pixel we are on doesn't need to be changed (don't want to change the 0s)
        if r < 0 or r > len(image) - 1 or c > len(image[0]) - 1 or c < 0 or image[r][c] != initial_pixel:
            return
        
        image[r][c] = color
        
        # Down
        self.fill(image, r + 1, c, initial_pixel, color)
        
        # Up
        self.fill(image, r - 1, c, initial_pixel, color)
        
        # Left 
        self.fill(image, r, c - 1, initial_pixel, color)
        
        # Right
        self.fill(image, r, c + 1, initial_pixel, color)
        
    # Time O(n)
    # Space O(n)