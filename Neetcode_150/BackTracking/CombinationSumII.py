"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""

#Come Back to this
#Tc=O(2^n) SC=O(2^n)


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def recursion(nums,i,op,sum):
            if sum==0:
                res.append(op)
                return
            if i==len(nums):
                return
            j=i
            while j+1<len(nums) and nums[j]==nums[j+1]:
                j=j+1
            same=op[:]
            op.append(nums[i])
            if nums[i]<=sum:
                recursion(nums,i+1,op,sum-nums[i])
                recursion(nums,j+1,same,sum)
            else:
                recursion(nums,j+1,same,sum)
            return
        recursion(candidates,0,[],target)
        return res