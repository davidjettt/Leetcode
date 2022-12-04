class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # [1, 2, 3, 4, 5] k=7 output: 1
        #              l r
   
        # Time O(n) where n is size of nums
        # Space O(n) where n is size of prefix_sums hashmap
        res = 0 # 2
        curr_sum = 0 # 3
        prefix_sums = {0: 1}
        
        for n in nums:
            curr_sum += n
            diff = curr_sum - k # 1
            # if diff exists in hashmap then that means we have valid subarrays with sum equal to k
            res += prefix_sums.get(diff, 0)
            # Increment number of prefix sums with curr_sum value
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
        
        return res
        