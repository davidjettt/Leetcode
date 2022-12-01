class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        [ 3, 6, 7, 11 ]  8
                   i         
                 k             
        1, 2, 3, 4, 5, 6, 7, 8 9, 10, 11
                 l  r                                    
        
        perform binary search from 1, max(piles)
        
            set a provisional k value
            
            test that k value by going though the array and calculating how long it takes koko to eat all the bananas
            
            if hours <= h
                then we have a valid k
                compare that with result (get the min)
                move right pointer
                
            hours > h
                not valid
                move left pointer
            
        return res
        
        Time O(logn * max(p)) where n is the max number of bananas and p is the size of piles array
        Space O(1)
        '''
        
        max_k = max(piles)
        res = max_k
        l, r = 1, max_k
        while l <= r:
            k = (r + l) // 2
            
            hours = 0
            for num_bananas in piles:
                hours += math.ceil(num_bananas / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
                
        
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
        