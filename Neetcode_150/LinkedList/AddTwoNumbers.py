"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
#TC= O(max(l1,l2)) SC=O(N) for the return Node
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        storage=0
        newNode=ListNode(-1)
        final=newNode
        while(l1 and l2):
            sum=l1.val+l2.val+storage
            if sum//10!=0:
                storage=sum//10
                sum=sum%10
            else:
                storage=0
            new=ListNode(sum)
            newNode.next=new
            newNode=newNode.next
            l1=l1.next
            l2=l2.next
        print(l1)
        print(l2)
        print(final)
        while l1:
            sum=l1.val+storage
            if sum//10!=0:
                storage=sum//10
                sum=sum%10
            else:
                storage=0
            new=ListNode(sum)
            newNode.next=new
            newNode=newNode.next
            l1=l1.next
        while l2:
            sum=l2.val+storage
            if sum//10!=0:
                storage=sum//10
                sum=sum%10
            else:
                storage=0
            new=ListNode(sum)
            newNode.next=new
            newNode=newNode.next
            l2=l2.next
        if storage==0:
            return final.next
        else:
            newNode.next=ListNode(storage)
            return final.next
            