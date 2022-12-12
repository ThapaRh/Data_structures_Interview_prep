"""Given an array arr[] of length N and an integer X, the task is to find the number of subsets with a sum equal to X.

Examples: 

Input: arr[] = {1, 2, 3, 3}, X = 6 
Output: 3 
All the possible subsets are {1, 2, 3}, 
{1, 2, 3} and {3, 3}

Input: arr[] = {1, 1, 1, 1}, X = 1 
Output: 4 """

def countSubsetSum(arr,target):
    dict = {}
    def count(arr,target,index):
        if target==0:
            return 1
        if index==0:
            return 0
        if (index,target) in dict:
            return dict[(index,target)]
        if arr[index-1]<=target:
            dict[(index,target)] = int(count(arr,target-arr[index-1],index-1)) + int(count(arr,target,index-1)) 
            return dict[(index,target)]
        else:
            dict[(index,target)] = int(count(arr,target,index-1))
            return dict[(index,target)]
    
    return count(arr,target,len(arr))

print(countSubsetSum([1,2,3],4))