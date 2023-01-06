"""
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

#Tc= )(2^n) SC= O(2^n) if we are making deep copy of every array, we would have n*n^2
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
           res=[]
           nums.sort()

           def recursion(nums,i,op):
                if i==len(nums):
                   res.append(op)
                   return
                notIncluded=op[:]
                op.append(nums[i])
                recursion(nums,i+1,op)

                #if I am ignoring 2 i need to ignore all th eupcoming 2's
                while(i+1<len(nums) and nums[i]==nums[i+1]):
                    i+=1
                recursion(nums,i+1,notIncluded)
                return
           recursion(nums,0,[])
           return res