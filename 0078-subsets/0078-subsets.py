class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        input is an integer array with unique elements
        need to return all possible subsets of array
        empty array is considered a subset

        [1,2,3]
             i

        '''
        # Time O(n * 2^n) where n is size of nums
        # Space O(n) 
        res = [[]]
        def backtrack(i, curr):
            if i >= len(nums):
                return
            
            curr.append(nums[i])
            res.append(curr.copy())
            # decision to include nums[i]
            backtrack(i + 1, curr)
            # decision to NOT include nums[i]
            curr.pop()
            backtrack(i + 1, curr)
            return

        backtrack(0, [])
        return res
        