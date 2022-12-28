"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

#Tc=O(N) SC=O(N) for recursive The extra space comes from implicit stack space due to recursion. The recursion could go up to nnn levels deep.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head,prev=None):
            if head==None:
               return prev
            next=head.next
            head.next=prev
            return rev(next,head)
        return rev(head,None)


#Tc=O(N) SC=O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        nxt=None
        while(curr!=None):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev

