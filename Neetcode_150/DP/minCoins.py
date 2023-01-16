"""You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1"""
#TC = O(sum*len(coins)) SC is same as well
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.least = math.inf
        length=len(coins)
        dict={}
        def recur(coins,i,sum):
            if sum==0:
                return 0
            if i>=length:
                return 100000
            if (i,sum) in dict:
                return dict[(i,sum)]
            if coins[i]<=sum:
                dict[(i,sum)] = min(1+recur(coins,i,sum-coins[i]),recur(coins,i+1,sum))
                return dict[(i,sum)]
            else:
                dict[(i,sum)] = recur(coins,i+1,sum)
                return dict[(i,sum)]
        val = recur(coins,0,amount)
        if val != 100000:
            return val
        else:
            return -1

#TC = O(N ) SC = O(N)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for i in range(amount+1)]
        dp[0]=0

        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i] = min(dp[i],1+dp[i-c])
        return dp[amount] if dp[amount]!=amount+1 else -1

