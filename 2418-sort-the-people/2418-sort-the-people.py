class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        # data = zip(heights, names)
        # data.sort(reverse=True)
        test = sorted(zip(heights,names), reverse=True)
        
        return [ n for h, n in test]
        
    
#         x, y = zip(*sorted(zip(heights, names), reverse=True))
        
#         return y