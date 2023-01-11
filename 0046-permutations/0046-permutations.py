class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        [1,2,3]

        [2,1,3], [2,3,1],
        [1,2,3], [1,3,2], 
        [3,1,2], [3,2,1]

        [1,2,3]
             i
            []
            /|\
           / | \
          1  2  3          
        /|   |\  |\
      /  |   | \ 31 32
     12  13  21 23 \  \
     |   |    |  | 312 321
     123  132 213 231

        how do i know if i reached bottom of tree
        base cases:
            if length of combo == length of nums
            if i pointer is greater than length of nums

            do i need to check for duplicates?
                no if i take care of that in backtracking code
            
        i = 0, [] -> [1]
        i = 1, [1] -> [1,2]
        i = 2, [1,2] -> [1,2,3] -
        i = 3, [1,2,3] -> return -

        i = 2, [1,2,3] -> [1,2]
        i = 3, [1,2] -> return


        i = 1, [1,2] -> [1]
        i = 2, [1] -> [1,3]
        i = 3, [1,3] -> return


        

        '''
        res = []
        if len(nums) == 1:
            return [nums.copy()]
        for i in range(len(nums)):
            n = nums.pop(0)

            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res