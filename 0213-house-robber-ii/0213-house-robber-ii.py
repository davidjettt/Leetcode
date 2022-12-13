class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        [4,4,3,1]
           i

        [2,3,2]
         i

        [1,2,3,1,4,2]

        [5,5,8,8,4,2]
               i

                  s
        [220,220,140,20,10]
                  i

        [200,3,140,20,10]
          i
        '''
        if len(nums) <= 3: return max(nums)
        
        def helper(arr):
            house1, house2 = 0, 0
            for curr_house in arr:
                temp = max(curr_house + house1, house2)
                house1 = house2
                house2 = temp
            return house2
        
        return max(helper(nums[1:]), helper(nums[:-1]))


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
        