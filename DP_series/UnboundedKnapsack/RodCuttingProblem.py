"""Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n.
 Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if the length of the rod is 8 and the values of
  different pieces are given as the following, then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20"""

def unboundedKnapsack(length,price):
    index = len(length)
    total = len(length)
    dict={}
    def cutRoad(length,price,index,total):
        if index==0 or len(length)==0 or len(price)==0:
            return 0
        if (index,total) in dict:
            return dict[(index,total)]
        if length[index-1]<=total:
            # print(length,price,index,total)
            dict[(index,total)] = max(price[index-1]+cutRoad(length,price,index,total-length[index-1]), cutRoad(length,price,index-1,total))
            return dict[(index,total)]
        else:
            # print()
            dict[(index,total)]= cutRoad(length,price,index-1,total)
            return dict[(index,total)]
        
    return cutRoad(length,price,index,total)

print(unboundedKnapsack([1,2,3,4,5,6,7,8],[1,5,8,9,10,17,17,20]))
print(unboundedKnapsack([1,2,3,4,5],[1,5,8,9,10]))

#now bottomup approach (not yet correct will do it later)

# def diffApproach(length,price):
#     sum = len(length)+1
#     len_price = len(length)+1
#     array=[[0 for i in range(sum)]for j in range(sum)]

#     for i in range(1,len_price+1): 
#         for j in range(1,sum+1):
#             if length[i-1]<=j:
#                 array[i][j]=max((price[i-1]+array[i][j-length[i-1]]), array([i-1][j]) )
#             else:
#                 array[i][j]=array([i-1][j])
#     return array[sum-1][len_price-1]

# print(diffApproach([1,2,3,4,5],[1,5,8,9,10]))

