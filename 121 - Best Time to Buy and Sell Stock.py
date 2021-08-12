def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


print(maxProfit(prices = [7,1,5,3,6,4]))
print(maxProfit(prices = [7,6,4,3,1]))
