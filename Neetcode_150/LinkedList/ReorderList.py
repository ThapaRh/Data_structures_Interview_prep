"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Time complexity: O(N)\mathcal{O}(N)O(N). There are three steps here. To identify the middle node takes O(N)\mathcal{O}(N)O(N) time. To reverse the second part of the list, one needs N/2N/2N/2 operations. The final step, to merge two lists, requires N/2N/2N/2 operations as well. In total, that results in O(N)\mathcal{O}(N)O(N) time complexity.

Space complexity: O(1)\mathcal{O}(1)O(1), since we do not allocate any additional data structures.
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return
        fast=head
        slow=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        #reversing the second half
        curr=slow
        nxt=None
        prev=None
        while(curr):
            nxt= curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        first=head
        second=prev
        while(second.next):
            # print(first)
            # print("////")
            # print(second)
            if first==second:
                break
            temp1=first.next 
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2

        #or easier way
        curr=head
        counter=0
        lst = ListNode(-1)
        while(curr and prev):
            if counter%2==0:
                lst.next=curr
                curr=curr.next
            else:
                lst.next=prev
                prev=prev.next
            counter+=1
            lst=lst.next
        return lst
