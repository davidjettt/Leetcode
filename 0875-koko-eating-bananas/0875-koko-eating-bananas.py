class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # k has to be between 1 - max number in the piles
        # b/c at most koko can eat at most k bananas
        # due to the constraints, it is guaranteed that koko will be able to eat all the bananas before the guards come back
        
        # will perform binary search between the range 1 - max number in the piles
        # k = # of bananas koko can eat / hr
        # to calcuate how many hrs it will take to eat a pile: Math.ceil(# number bananas in pile / k )
        
        
        # will do binary search as long as left pointer is <= right pointer
        
        # at each iteration we will calculate number of hrs it takes to eat each pile in piles and add them all up and then compare with the hrs input
        
        # if find valid k value --> move right pointer to the left
            # and also compare with result variable, get the min 
        # if find invalid k value --> move left pointer to the right
        
        # [ 3, 6, 7, 11 ]
        #   1. 1  2  2
        #   1. 2  3  4
        #   1  2  2  3
        
        #  k =   1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 
        #.                lm r                 
        
        
        # Time O(log(max(p) )* p) where p is the size of piles
        # Space O(1)
        max_k = max(piles)
        res = max_k  # 6
        left, right = 1, max_k
        
        while left <= right:
            k = (left + right) // 2  # 4
            
            curr_hrs = 0 # 8
            
            for pile in piles:
                curr_hrs += math.ceil(pile / k) # 11 / 4
            
            if curr_hrs <= h:
                res = min(res, k)
                
                right = k - 1
            else:
                left = k + 1
                
        
        return res
        