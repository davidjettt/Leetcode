class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # initialize result array and count variable
        # loop through array and at each iteration add to count, and then push count to result array
        
        
        sums = []
        count = 0
        
        for n in nums:
            count += n
            sums.append(count)
            
        return sums