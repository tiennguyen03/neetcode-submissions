class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        l,r = 0, 1
        best_sell = 0 


        while r < len(prices):

            if(prices[l] > prices[r]):
                l += 1
                r = l
            
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
                
            r += 1
        
    
        return max_profit

    