"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
"""
#TC=O(logN) SC=O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
             # code here
        n=len(nums)
        start=0
        end = n-1
        while(start<=end):
            mid=(start+end)//2
            prev=(mid-1+n)%n #to make sure that if we are 0th index, we rotate and reach to end index cause the numsay is rotating numsay
            next=(mid+1)%n
            if nums[mid]<=nums[prev] and nums[mid]<=nums[next]:
                return nums[mid]
            if nums[0]<=nums[mid]:
                start=mid+1
            elif nums[mid]<=nums[n-1]:
                end=mid-1
        return nums[0]