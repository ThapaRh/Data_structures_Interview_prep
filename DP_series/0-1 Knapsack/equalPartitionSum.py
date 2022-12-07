# 416. Partition Equal Subset Sum
# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# TC : O(m*n) where m is the max_size and n is th elength of weight array
# SC: O(m*n) basically the same. 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        lengthal = sum(nums)
        dp_dict = {}
        def subset_check(arr,target,length):
            if length==0:
                return False
            if target==0:
                return True
            if (target,length) in dp_dict:
                return dp_dict[(target,length)]
            else:
                if arr[length-1]<=target:
                    dp_dict[(target,length)] = subset_check(arr,target,length-1) or subset_check(arr,target-arr[length-1],length-1)
                    return dp_dict[(target,length)]
                else:
                    return subset_check(arr,target,length-1)

        if lengthal%2 ==1 :
            return False
        else:
            return subset_check(nums,lengthal//2,len(nums))