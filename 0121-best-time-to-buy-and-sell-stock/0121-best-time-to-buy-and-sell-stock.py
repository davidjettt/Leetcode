class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # [1,2,3,2,5,7,2,4,9,0,9]
        #  l                 r
        
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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # have array of prices of a stock with index = day
        # need to return max profit between 2 prices in the array
        # must buy first and then sell
        # Buying index has to be lower than selling index
        # if not profit possible aka array with decreasing values then return 0
        
        # day = 1
        
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

        
#         left = 0
#         right = 1
#         max_profit = 0
        
#         while right < len(prices):
            
#             current_profit = prices[right] - prices[left]
            
#             if current_profit > max_profit:
#                 max_profit = current_profit
            
#             elif current_profit < 0:
#                 left = right
            
#             right += 1
                
#         return max_profit
            
        
        # Time O(n)
        # Space O(1)