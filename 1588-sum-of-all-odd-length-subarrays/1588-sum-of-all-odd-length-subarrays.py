class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        prefix_sum = [arr[0]]
        
        for i in range(1, len(arr)):
            prefix_sum.append(prefix_sum[-1] + arr[i])
            
        res = 0
        
        for start in range(len(arr)):
            # end = start
            for end in range(start, len(arr), 2):
                if start == 0:
                    res += prefix_sum[end]
                else:
                    res += prefix_sum[end] - prefix_sum[start - 1]
                
#             while end < len(arr):
#                 if start == 0:
#                     res += prefix_sum[end]
#                 else:
#                     res += prefix_sum[end] - prefix_sum[start - 1]
                
#                 end += 2
        return res
    
        
    
#         res = 0
#         if len(arr) % 2 != 0:
#             res = sum(arr)
            
        
#         left = 0
        
#         for right in range(len(arr)):
#             res += arr[right]
            
#             while (right - left + 1) % 2 != 0 and left < right:
#                 res += arr[left]
#                 left += 1
            
#             res += arr[left]
        
#         return res