"""
121. Best Time to Buy and Sell Stock
Easy
22K
695
company
Amazon
company
Adobe
company
Apple
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
#BruteForec TC: O(n^2)
#2nd approach TC: O(N)
#Here we have to find a solution that has minimum buy  price and maximum sell price. 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit=0
        # for i in range(len(prices)):
        #     for j in range(i,len(prices)):
        #         calc=prices[j]-prices[i]
        #         max_profit=max(max_profit,calc)
        # return max_profit

        left=0
        right=1
        max_profit=0
        while(right<len(prices)):
            if prices[right]<=prices[left]:
                left=right
                right+=1
            else:
                curr= prices[right]-prices[left]
                max_profit=max(curr,max_profit)
                right+=1
        return max_profit
