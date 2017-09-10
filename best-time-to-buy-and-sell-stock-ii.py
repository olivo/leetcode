class Solution(object):
    def maxProfit(self, prices):
        profits = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profits += prices[i] - prices[i - 1]

        return profits