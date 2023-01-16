"""

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

"""

# TC = O(n) cause we have to iterate through this
#SC = O(n) : dictionary
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict={}
        for num in nums:
            if num in dict:
                return True
            else:
                dict[num]=1
        return False




# this is different approach with TC: O(nlog(n)) and SC: O(1) by sorting
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        print(nums)
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False
