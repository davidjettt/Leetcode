class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        
#         allNums = []
        
#         for i in range(1, len(nums) + 1):
#             allNums.append(i)
            
        
#         for n in allNums:
#             if n not in nums:
#                 return n
        
#         return 0
            
    
    # initial missingNum variable set to 0
    # sort the nums array
    # [ 0, 1, 3 ]
    # loop through nums array
    # if n is not equal to missingNum
        # misssingNum ++
        # go to next iteration
    # else return missingNum
    
    # [ 0, 1 ]
    
        missingNum = 0 
        nums.sort()

        for n in nums:
            if n == missingNum:
                missingNum += 1
            else:
                return missingNum
                # missingNum += 1
        return missingNum
    