"""
Given a binary tree, determine if it is 
height-balanced
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true
"""
#Tc= O(N) Sc=if balanced O(logN) but if not O(N)
#  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalancedII(root):
            if root==None:
                return [True,0]
            left=isBalancedII(root.left)
            right=isBalancedII(root.right)
            balanced = left[0] and right[0] and (abs(left[1]-right[1])<=1)
            ret=1+max(left[1],right[1])
            return [balanced, ret] 
        val=isBalancedII(root)
        return val[0]
