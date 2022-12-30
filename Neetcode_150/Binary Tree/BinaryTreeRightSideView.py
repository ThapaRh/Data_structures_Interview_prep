"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
"""
#TC=O(N) Sc=O(N)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q=collections.deque([root])
        new_array=[]

        while(q): #when the queue is not empty cause we iterate till queue is empty
            rightside=None #this stores the rightmost element in queue
            length=len(q)

            for i in range(length): #This is for the level....each for loop is one level cause with each length we get one level worth of data
                v = q.popleft() #left bata udaudai jane 

                if v: #tyo left wala nonempty ho vane values add garne
                    rightside=v
                    q.append(v.left)
                    q.append(v.right)
            if rightside: #ani tyo for loop sakesi, rightmost ma sabse right ko bashxa, tei halne hamro array ma
                new_array.append(rightside.val)
        return new_array
