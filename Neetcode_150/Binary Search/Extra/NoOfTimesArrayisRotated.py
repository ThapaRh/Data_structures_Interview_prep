"""
Given an ascending sorted rotated array Arr of distinct integers of size N. The array is right rotated K times. Find the value of K.

Example 1:

Input:
N = 5
Arr[] = {5, 1, 2, 3, 4}
Output: 1
Explanation: The given array is 5 1 2 3 4. 
The original sorted array is 1 2 3 4 5. 
We can see that the array was rotated 
1 times to the right.
"""
#TC=O(logN) SC=O(1)
#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        start=0
        end = n-1
        while(start<=end):
            mid=(start+end)//2
            prev=(mid-1+n)%n #to make sure that if we are 0th index, we rotate and reach to end index cause the array is rotating array
            next=(mid+1)%n
            if arr[mid]<=arr[prev] and arr[mid]<=arr[next]:
                return mid
            if arr[0]<=arr[mid]:
                start=mid+1
            elif arr[mid]<=arr[n-1]:
                end=mid-1
        return 0