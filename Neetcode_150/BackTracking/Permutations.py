"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
#TC= O(N^2 maybe not sure) SC=O(N!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def recursionPermutation(nums,permutation,used):
            if len(permutation)==len(nums):
                res.append([n for n in permutation])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i]=True
                    permutation.append(nums[i])
                    recursionPermutation(nums,permutation,used)
                    used[i]=False
                    permutation.pop()
        recursionPermutation(nums,[],[False for i in range(len(nums))])
        return res
