"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
#This i supdated version of two sum using two pointes
TC=O(N^2) SC= O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        start=0
        end=len(nums)-1
        nums.sort()
        final_array=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            start=i+1
            end=len(nums)-1
            while(start<end):
                sum = nums[start] + nums[end] + nums[i]
                if sum>0:
                    end-=1
                elif sum<0:
                    start+=1
                else:
                    final_array.append([nums[i],nums[start],nums[end]])
                    start+=1
                    while nums[start]==nums[start-1] and start<end: # cause we dont want duplicate triplets even if there are duplicate triplets
                        start+=1
        return final_array







"""
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

 

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
"""
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count=0
        nums.sort()
        for i in range(len(nums)):
            start=i+1
            end=len(nums)-1
            while(start<end):
                sum=nums[i]+nums[start]+nums[end]
                if sum<target:
                    count+=(end-start)
                    start+=1
                else:
                    end-=1
                
        return count