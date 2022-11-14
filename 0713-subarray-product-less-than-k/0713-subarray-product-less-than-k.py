class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # res = 1 + 2 + 2 + 3
        # [10,5,2,6]
        #     l r
        
        # [1,2,3] k=0
        #  lr
            
        res = 0 
        curr_product = 1  
        l = 0
        
        for r in range(len(nums)):
            curr_product *=  nums[r]
            if curr_product < k:
                res += (r - l + 1)
            else:
                while curr_product >= k and l < len(nums):
                    curr_product //= nums[l]
                    l += 1
                
                # if curr_product < k:
                #     res += (r - l + 1)
                res += (r - l + 1)
        return 0 if res < 0 else res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # sliding window
        # init res variable that counts number of valid subarrays
        # init currProduct variable that checks product of each window
        # init left pointer var 
        # loop through nums array
        # at each iteration, check if right value times currProuct < k
            # if true, add length of window to res variable
            # if false, need to move left pointer until currProduct < k 
            # also before moving left pointer need to divide currProduct by that number
        
        # Time O(n) where n is number of times iterating nums array
        # Space O(1)
        # res = 0
        # curr_product = 1
        # left = 0
        # for right in range(len(nums)):
        #     curr_product *= nums[right]
        #     while curr_product >= k and left < len(nums):
        #         curr_product //= nums[left]
        #         left += 1
        #     if right >= left:
        #         res += right - left + 1
        # return res