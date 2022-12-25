"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
#TC=O(logN) SC=O(k)
#Go back and have a look at alternate solution. Right now brain is malfunctioning. I need food and full time job lol. This is fucking stressful sometimes when you fucking don't unserstand how code works bitch. It's only fun if your brain  is cooperating. Yesterday my brain was and today it's like lemme make you suffer. Tf bitch tf.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        n=len(nums)
        minIndex=0
        while(start<=end):
            mid=(start+end)//2
            prev=(mid-1+n)%n 
            next=(mid+1)%n
            if nums[mid]<=nums[prev] and nums[mid]<=nums[next]:
                minIndex=mid
            if nums[0]<=nums[mid]:
                start=mid+1
            elif nums[mid]<=nums[n-1]:
                end=mid-1
        def binarySearch(array,start,end):
            mid=(start+end)//2
            if(start>end):
                return -1
            if target==array[mid]:
                return mid
            elif array[mid]>target:
                return binarySearch(array,start,mid-1)
            elif target>array[mid]:
                return binarySearch(array,mid+1,end)
        if target==nums[minIndex]:
            return minIndex
        val1=binarySearch(nums,0,minIndex-1)
        val2=binarySearch(nums,minIndex+1,n-1)
        return max(val1,val2)