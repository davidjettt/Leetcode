class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        # [
        #     [1,1,0],
        #     [1,0,1],
        #     [0,0,0]
        # ]
        
        # Time O(n^2n)   Space O(1)
#         for i in range(len(image)):
#             image[i].reverse()
#             for j in range(len(image[i])):
#                 if image[i][j] == 1:
#                     image[i][j] = 0
#                 else:
#                     image[i][j] = 1
        
#         return image
        
        return [ [x ^ 1 for x in reversed(row)] for row in image ]
        
#         for i in range(len(image)):
#             image[i].reverse()
            
            
#         row = 0
#         col = 0
#         row_length = len(image[0])
        
#         while row < len(image):
            
#             if image[row][col] == 1:
#                 image[row][col] = 0
#             else:
#                 image[row][col] = 1
                
#             col += 1
            
#             if col == row_length:
#                 col = 0
#                 row += 1
        
#         return image