"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

"""
Time complexity: O(n*2^n) to generate all subsets and then copy them into output list.

Space complexity:  O(n*2^n) to keep all the subsets of length N, since each of N elements could be present or absent.
"""
class Solution(object):
    def subsets(self, nums):
        res=[]
        dict={}
        # op=[1,2,3]
        # ap=op[:]
        # op.append(1)
        # print(op,ap)

        def unique(ip,op):
            if len(ip)==0:
                res.append(op)
                return
            val = op[:]
            op.append(ip[0])
            return unique(ip[1:],op) or unique(ip[1:],val)
        unique(nums,[])
        return res