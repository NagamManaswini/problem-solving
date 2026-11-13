class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_stock=prices[0]
        profit=0
        for i in prices[1:]:
            if buy_stock>i:
                buy_stock=i
            profit=max(profit,i-buy_stock)
        return profit

