class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        # [
        #     [1,1,0],
        #     [1,0,1],
        #     [0,0,0]
        # ]
        
        
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[i])):
                # print(image[i][j])
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
        
        return image
                