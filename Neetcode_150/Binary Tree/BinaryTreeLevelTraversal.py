"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
"""
#TC=O(N)  SC=O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dictionary={}
        def eachlevel(root,level):
            if root==None:
                return 
            if level in dictionary:
                dictionary[level].append(root.val)
            else:
                dictionary[level]=[root.val]
            eachlevel(root.left,level+1)
            eachlevel(root.right,level+1)
        eachlevel(root,0)
        return dictionary.values()