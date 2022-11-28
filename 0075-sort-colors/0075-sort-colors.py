class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        
        [0,0,1,1,2,2]
             l m  h
        
        [0,0,0,1,1,2,2,2]
             l       mh  
             
             
        [0, 1, 2]
           lh  m   
           
        [ 0, 1, 2 ]
            lh m 
           
           
        [0, 1, 2, 1, 0, 2, 1, 2] 
        l   m              h
        
        looping as long as mid < high
        
            if mid points to 2: swap with what high is pointing to and move high
            if mid points to a 0: swap with what low is pointing to and move low
            do nothing when mid points to 1
        
        '''
        
        low, mid, high = 0, 0, len(nums) - 1
        
        
        while mid <= high:
            if nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            elif nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            else:
                mid += 1
        
            # if nums[low] == 0:
            #     low += 1
            
            # mid += 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
#         mid, low, high = 0, 0, len(nums) - 1
        
#         while mid <= high:
            
#             if nums[mid] == 2:
#                 nums[high], nums[mid] = nums[mid], nums[high]
                
#                 high -= 1
            
#             elif nums[mid] == 0:
#                 nums[low], nums[mid] = nums[mid], nums[low]
                
#                 low += 1
#                 mid += 1
            
#             else:
#                 mid += 1
                