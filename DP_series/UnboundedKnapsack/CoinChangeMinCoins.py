"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

#!!!!!!!!!!!!!!!!!!!!!!!!!!Not 100% Correct

class Solution(object):
    def coinChange(self, coins, amount):
        coins.sort()
        dict={}
        
        def countMinimun(coins,amount,arraylength,minamt):
            if arraylength==0:
                return 1000000
            if amount==0:
                return minamt
            if (amount,arraylength) in dict:
                return dict[(amount,arraylength)]
            if coins[arraylength-1]<=amount:
                dict[(amount,arraylength)]= min(countMinimun(coins,amount-coins[arraylength-1],arraylength,minamt+1) , countMinimun(coins,amount,arraylength-1,minamt))
                return dict[(amount,arraylength)]
            else:
                dict[(amount,arraylength)] = int(countMinimun(coins,amount,arraylength-1,minamt))
                return dict[(amount,arraylength)]
        
        storage =  countMinimun(coins,amount,len(coins),0)
        if storage!=1000000:
            return storage
        else:
            return -1