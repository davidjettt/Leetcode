class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time O(n)
        # Space O(1)
        max_profit = 0
        
        low, high = 0, 1
        
        while high < len(prices):
            curr_profit = prices[high] - prices[low]
            
            if prices[high] > prices[low]:
                max_profit = max(max_profit, curr_profit)
            else:
                low = high
            high += 1
        
        return max_profit
        
        
#         left = 0 #buy
#         right = 1  # sell
#         max_profit = 0
        
#         while right < len(prices):
#             current_profit = prices[right] - prices[left]
            
#             if prices[left] < prices[right]:
#                 max_profit = max(current_profit, max_profit)
#             else:
#                 left = right
                
#             right += 1
            
#         return max_profit