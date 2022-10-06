class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time O(2n) Space O(n)
        counts = {}
        
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        res = 0
        majority = 0
        
        for num in counts:
            if counts[num] > majority:
                majority = counts[num]
                res = num
        return res

        