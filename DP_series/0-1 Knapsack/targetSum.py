"""
Given an array arr[] of size N and a given difference diff, the task is to count the number of partitions that we can perform 
such that the difference between the sum of the two subsets is equal to the given difference.

Note: A partition in the array means dividing an array into two parts say S1 and S2 such that the union of S1 and 
S2 is equal to the original array and each element is present in only of the subsets.
"""
#These two are basically same questions
"""You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3"""

class Solution(object):
    def findTargetSumWays(self, nums, target):
        sums = sum(nums)
        if (sums+target)%2!=0:
            return 0
        new_target = (sums + target)/2
        dict = {}
        def count(arr,target,index):
            if index==0:
                if target==0:
                    return 1
                return 0
            if (index,target) in dict:
                return dict[(index,target)]
            if arr[index-1]<=target:
                dict[(index,target)] = int(count(arr,target-arr[index-1],index-1)) + int(count(arr,target,index-1)) 
                return dict[(index,target)]
            else:
                dict[(index,target)] = int(count(arr,target,index-1))
                return dict[(index,target)]
        return count(nums,new_target,len(nums))