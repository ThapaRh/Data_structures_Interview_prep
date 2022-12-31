"""
  Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""
#TC=O(N) SC=O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        value = preorder[0]
        middleIndex= inorder.index(value)
        tree = TreeNode(value)
        tree.left=self.buildTree(preorder[1:middleIndex+1],inorder[:middleIndex])
        tree.right=self.buildTree(preorder[middleIndex+1:],inorder[middleIndex+1:])
        return tree

        