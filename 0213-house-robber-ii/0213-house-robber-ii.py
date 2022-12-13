class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        '''
        # if len(nums) <= 3: return max(nums)
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, arr):
        house1, house2 = 0, 0
        for curr_house in arr:
            temp = max(curr_house + house1, house2)
            house1 = house2
            house2 = temp
        return house2


        # if len(nums) <= 3:
        #     return max(nums)

        # for i in range(len(nums) - 2): # 3  0 1 2 
        #     if i == 0:
        #         nums[i] = max(nums[i] + nums[-2], nums[-1])
        #     elif i == 1:
        #         nums[i] = max(nums[i] + nums[-1], nums[i - 1])
        #     else:
        #         nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        # return nums[-3]
        