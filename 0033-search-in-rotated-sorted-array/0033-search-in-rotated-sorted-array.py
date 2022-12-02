class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        
        nums can possibly be rotated
        we dont know the pivot index, but if nums is rotated then pivot value is nums[0]
        
        [1,2,3,4]
           k
        [2,3,4,1]
             k  
        
        [2,3,4,5]
             k
             
        [4,5,2,3]
           k
             
        [0,1,2,4,5,6,7]
               k
               
               
               
        [4,5,6,7,0,1,2]    t = 0
         l     m     r
        
        '''
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (r + l) // 2
            
            if target == nums[mid]: return mid
        
            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
        