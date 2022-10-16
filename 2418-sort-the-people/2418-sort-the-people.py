class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
#         [ Mary, John, Emma ]

#         [ 180, 165, 170 ]

#         {
#             180: Mary,
#             165: John,
#             170: Emma
#         }
        
#         lookup = {}
        
#         for i in range(len(heights)):
            
#             if heights[i] not in lookup:
#                 heights[i] = names[i]
        
#         res = []
#         data = list(zip(heights, names))
#         data.sort(reverse=True)

        
#         for h, n in data:
#             res.append(n)
            
#         return res
    
        x, y = zip(*sorted(zip(heights, names), reverse=True))
        
        return y