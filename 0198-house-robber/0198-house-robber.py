class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
         0 1 2 3
        [1,2,3,1]

         0 1 2 3 4
        [2,7,9,3,1]

            0(1)
            /\
         2(3)  3(1)
         /      /

         [2,1,1,2]
        '''
        # for i in range(1,len(nums)):
        #     if i == 1:
        #         nums[i] = max(nums[i], nums[i - 1])
        #     else:
        #         nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        # return nums[-1]
        
        house1, house2 = 0, 0
        
        for curr_house in nums:
            temp = max(curr_house + house1, house2)
            house1 = house2
            house2 = temp
        return house2
    
