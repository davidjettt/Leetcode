class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counts = {}
        
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        
        res = 0
        majority = 0
        print(counts.items())
        for num, count in counts.items():
            if count > majority:
                majority = count
                res = num
        
        return res
        