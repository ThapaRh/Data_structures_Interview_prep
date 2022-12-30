"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
"""
#TC=O(N)  Sc= worst case is O(N) and O(log(n)) for the best case or average case 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        elif p==None:
            return False
        elif q==None:
            return False
        if p.val!=q.val:
            return False
        right=self.isSameTree(p.right,q.right)
        left=self.isSameTree(p.left,q.left)
        return right and left