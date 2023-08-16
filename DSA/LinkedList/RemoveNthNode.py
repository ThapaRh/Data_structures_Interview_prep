
#SC= O(1) TC=O(n)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        if head == None:
            return None
        if head.next == None and n==1:
            return None
        while curr:
            count+=1
            curr=curr.next
        target = count-n
        final = head
        c = 1
        if target == 0:
            head = head.next
            return head
        while(c<target):
            final=final.next
            c+=1
        final.next = final.next.next
        return head
    
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = ListNode(-1,head)
        dummy = slow
        if head == None:
            return None
        i=0
        while(i<n):
            fast = fast.next
            i+=1
        while(fast):
            slow=slow.next
            fast=fast.next
        if slow and slow.next:
            slow.next=slow.next.next
        return dummy.next