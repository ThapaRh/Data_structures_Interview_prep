
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''
#TC = O(N) Sc=O(N)
class Solution:
    def trap(self, height: List[int]) -> int:
        i=1
        max_left = [0 for i in range(len(height))]
        max_right = [0 for i in range(len(height))]
        #finding the maximun height in the left
        while(i<len(height)):
            if height[i-1]>max_left[i-1]:
                max_left[i] = height[i-1]
            else:
                max_left[i] = max_left[i-1]
            i+=1
        
        i = len(height)-2
        #finding the maximum height in the right
        while(i>=0):
            if height[i+1]>max_right[i+1]:
                max_right[i]=height[i+1]
            else:
                max_right[i] = max_right[i+1]
            i-=1
        #finding the minimum of max_left and right and summing
        total_water = 0
        for i in range(len(height)):
            minimum_left_right = min(max_left[i],max_right[i])
            difference=  minimum_left_right-height[i]
            if difference>0:
                total_water+=difference
        return total_water
            