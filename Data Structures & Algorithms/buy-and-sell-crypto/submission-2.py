class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dynamic window

        end = 0
        start = 0
        profit = 0

        window keeps expanding until it reaches a higher profit
        when a new minimum is found, move to that minimum
       
        """
        start = 0
        maxProfit = 0
        profit = 0

        for end in range(1, len(prices)):
            
            profit = prices[end] - prices[start] 
            maxProfit = max(profit, maxProfit)

            # find new minimum
            if prices[end] < prices[start]:
                start = end

           
        return maxProfit