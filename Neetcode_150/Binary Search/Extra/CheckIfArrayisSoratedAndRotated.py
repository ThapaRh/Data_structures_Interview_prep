"""
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
"""
#TC=O(N) SC=O(1)
class Solution:
    def check(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)):
            if nums[i]<nums[i-1]:
                print(nums[i])
                print(nums[i-1]) # And in python [0-1] is -1 whuch is the last element of stack and hence it will do rotation itself. This shit got me stuck for 1hr and 18 fucking minutes.
                count+=1
        if count<=1:
             #because in rotated array there can only be once that next elem is less than prev, in the roattion index 
            return True
        else:
            return False