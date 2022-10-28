class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding window
        # init res variable that counts number of valid subarrays
        # init currProduct variable that checks product of each window
        # init left pointer var 
        # loop through nums array
        # at each iteration, check if right value times currProuct < k
            # if true, add length of window to res variable
            # if false, need to move left pointer until currProduct < k 
            # also before moving left pointer need to divide currProduct by that number
            
        # currProduct = 50
        # [ 10, 5, 2, 6 ]
        #.  l      r
        
        # [ 1, 2, 3 ]    k = 0
        #  lr 
        
        res = 0
        curr_product = 1
        left = 0
        for right in range(len(nums)):
            curr_product *= nums[right]
            while curr_product >= k and left < len(nums):
                curr_product //= nums[left]
                left += 1
            if right >= left:
                res += right - left + 1
#             if curr_product < k:
#                 res += (right - left + 1)
#             else:
#                 while curr_product >= k and left < len(nums):
#                     curr_product //= nums[left]
                    
#                     left += 1
#                 res += (right - left + 1)
        return res