class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l, r, max_val = 0, 1, 0


        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         max_val = max(max_val, profit)
        #     else:
        #         l = r
        #     r += 1
        # return max_val

        min_pr=prices[0]
        max_pr=0
        for price in prices:
            if price < min_pr:
                min_pr = price
            profit = price-min_pr
            if profit > max_pr:
                max_pr = profit
        return max_pr
