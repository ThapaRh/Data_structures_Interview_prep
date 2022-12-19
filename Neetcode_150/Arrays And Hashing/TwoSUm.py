"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

#TC= O(n) because lookup in hashtable is O(1) SC= O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=[i]
            else:
                dict[nums[i]].append(i)
        for j in range(len(nums)):
            storage = target-nums[j]
            print(storage)
            if storage in dict and dict[storage][0]!=j:
                return [j,dict[target-nums[j]][0]]
        return [0,0]

