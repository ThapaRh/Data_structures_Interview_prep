#https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/
"""Tc = O(n)    SC=O(1)"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return None
        if head.next:
            fast = head.next.next
            slow = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        if slow and slow.next:
            slow.next = slow.next.next
        return head