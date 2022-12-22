"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""
#TC=O(n) SC=O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        maximum=0
        while(start<end):
            if height[start]>height[end]:
                storage=height[end]*(end-start)
                maximum=max(maximum,storage)
                end-=1
            elif height[end]>=height[start]:
                storage=height[start]*(end-start)
                maximum=max(maximum,storage)
                start+=1
        return maximum


#This is bruteforce with TC=O(N^2)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum=0
        for i in range(len(height)):
            for j in range(i,len(height)):
                storage = min(height[i],height[j])*(j-i)
                maximum=max(storage,maximum)
        return maximum
