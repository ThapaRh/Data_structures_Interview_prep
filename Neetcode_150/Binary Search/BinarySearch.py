"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""
#TC=O(logN) SC=O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
       start = 0
       end=len(nums)-1
       while(start<=end):
           mid=(start+end)//2
           if nums[mid]==target:
               return mid
           elif nums[mid]>target:
                end = mid-1
           elif nums[mid]<target:
                start=mid+1
       return -1