
"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
Example 1:
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
"""

#TC=O(lenofTree *length of subtree) and SC=O(N)O(MN). For every NNN node in the tree, we check if the tree rooted at node is identical to subRoot. This check takes O(M)O(M)O(M) time, where MMM is the number of nodes in subRoot. Hence, the overall time complexity is O(MN)O(MN)O(MN).

#Space complexity: O(M+N)

#There will be at most NNN recursive call to dfs ( or isSubtree). Now, each of these calls will have MMM recursive calls to isIdentical.
#  Before calling isIdentical, our call stack has at most O(N) elements and might increase to O(N+M) during the call. 
# After calling isIdentical, it will be back to at most O(N) since all elements made by isIdentical are popped out. Hence, the maximum number of elements in the call stack will be M+N.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def check(p,q):
            if p==None and q==None:
                return True
            elif p==None:
                return False
            elif q==None:
                return False
            if p.val!=q.val:
                return False
            right=check(p.right,q.right)
            left=check(p.left,q.left)
            return right and left


        if subRoot==None: # we are given that tree and subtree is nonempty but in case if they were empty
            return True
        if root==None:#it has to be the second if, only when subroot is nonempty and root is empty return False
            return False
        value=False
        if root.val==subRoot.val:
            value = check(root,subRoot)
        if value:
            return value
        else:
            return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
