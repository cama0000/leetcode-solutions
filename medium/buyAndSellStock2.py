class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy any time the stock is greater than the last day

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit