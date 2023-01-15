"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

# !!!!!!!!!!!!!!!!!!!!!!!!!!100% Correct
# it didnot work before when I passed minimum number of coins as a parameter, but if I don't pass it as parameter and sum it within minimum calculation like when in line 32, then there is no error.
class Solution(object):
    def coinChange(self, coins, amount):
        dict={}
        
        def countMinimun(coins,amount,arraylength):
            if arraylength==0:
                return 1000000
            if amount==0:
                return 0
            if (amount,arraylength) in dict:
                return dict[(amount,arraylength)]
            if coins[arraylength-1]<=amount:
                dict[(amount,arraylength)]= min(1+countMinimun(coins,amount-coins[arraylength-1],arraylength) , countMinimun(coins,amount,arraylength-1))
                return dict[(amount,arraylength)]
            else:
                dict[(amount,arraylength)] = int(countMinimun(coins,amount,arraylength-1))
                return dict[(amount,arraylength)]
        
        storage =  countMinimun(coins,amount,len(coins))
        if storage!=1000000:
            return storage
        else:
            return -1


"""
------> sum
|
|
|
|
|
This is length array

Basically horizontal is sum and vertical is length of array

"""

#####Time Limit exceeded for this one, go through this again later

# def coinChange(coins, amount):
#     #initialize the array
#     table = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
#     for i in range(len(coins)+1):
#         table[i][0]=0
#     for j in range(amount+1):
#         table[0][j]= 1000000
#     for j in range(1,amount+1):
#         if j%coins[0]==0:
#             table[1][j]=int(j/coins[0])
#         else:
#             table[1][j]=1000000
#     print(table)
#     for i in range(1,len(coins)+1):
#         for j in range(1,amount+1):
#             if coins[i-1]<=j:
#                 table[i][j]=min(1+table[i][j-coins[i-1]],table[i-1][j])
#             else:
#                 table[i][j]=table[i-1][j]
#     return table[i][j]

# print(coinChange([6,2,4,1],6))

