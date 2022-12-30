"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
"""
#TC= O(N) SC: O(N) worst case average case is O(logN)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root,mini,maxi):
            if root==None:
                return True
            if root.val>=maxi or root.val <=mini:
                return False
            return helper(root.left,mini,root.val) and helper(root.right,root.val,maxi)
        return helper(root,-math.inf,math.inf)