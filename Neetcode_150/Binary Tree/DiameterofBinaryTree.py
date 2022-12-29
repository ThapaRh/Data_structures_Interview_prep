"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
"""
#TC= O(N) SC= Space complexity: O(N)O(N)O(N). The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. In the worst case, 
# the tree is skewed so the height of the tree is O(N)O(N)O(N). If the tree is balanced, it'd be O(log⁡N)O(\log N)O(logN).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter=0
        def maxLength(root):
            if root==None:
                return -1
            left_height=maxLength(root.left)
            right_height=maxLength(root.right)
            diameter= 2+ left_height+right_height
            self.max_diameter=max(self.max_diameter,diameter)
            total_height= 1+ max(left_height,right_height)
            return total_height
        maxLength(root)
        return self.max_diameter