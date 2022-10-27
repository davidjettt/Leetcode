class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
#         [[ 1, 3 ], [ 6, 9 ]]
        
        
#         [ 2, 5 ]
        
        # Set up result array
        
        # set up boolean variable = False
        
        # loop through intervals list
        # at each iteration check if newInterval[0] is between intervals[i][0] and intervals[i][1]
            
            # if it is in between, then change boolean variable to True
            
            # else then push into result array and continue with next loop
            
            # set up another conditional that says if boolean variable is True execute this code
                
                # if True, then at every next iteration check if newInterval[1] is less than intervals[i][1]
                    # if False, then keep searching ( pop off that subarray )
                    
                    # if True, then new interval would be the first start interval when we changed boolean variable and the end interval at this current iteration (would need to change subarray to those vals)
                    
                    # then break from loop
                    # return intervals
                    # change boolean variable back to False so that code will execute at next loop which will push any remaining intervals into result array
        
        # Time O(n) where in is length of input array
        # Space O(n) where n is length of result array
        res = []
        
        for i in range(len(intervals)):
            # if end of new interval is less than start of current interval in iteration
            # if true, that means there is no overlap and new interval comes first so append to result array
            # and then we can slice the rest of the array from i and add to end of result array
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if start of new interval is greater than end of current interval
            # that means new interval comes after so we can append current interval to result array
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                # changes new interval
                # start is the lowest between new and current
                # end is the highest between new and current
                newInterval = [ min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1]) ]
        
        # this runs if new interval goes at the very end
        res.append(newInterval)
        
        return res
        
                    
#         is_between = False
#         new_start = None
#         res = []
#         merged = []
#         for sub in intervals:
            
#             if len(merged):
#                 if newInterval[1] > sub[0]:
#                     merged[1] = max(newInterval[1], sub[1])
#                     res.append(merged)
#                 else:
#                     res.append(sub)
                    
#             else:
#                 # checks if start of new interval is in between interval in list
#                 if sub[0] <= newInterval[0] <= sub[1]:
#                     # is_between = True
#                     # continue
#                     merged.append(min(sub[0], newInterval[0]))
#                     # res.append(merged)

#                 else:
#                     res.append(sub)
                
    
            
        # return res