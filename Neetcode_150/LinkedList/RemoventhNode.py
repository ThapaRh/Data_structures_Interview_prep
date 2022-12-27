"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

#TC for both is O(length of ll) and SC= O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start=ListNode(-1, head)
        dummy=start # for the questions like [1] remove 1, we need dummy because we will have deleted the head itself
        end=head#we wanna keep this n steps ahead of start because we need to delete nth item.
        while(n>0 and end!=None):
            end=end.next
            n-=1
        print(start)
        while(end!=None):
            start=start.next
            end=end.next
        print(start)
        if start and start.next:
            start.next=start.next.next  
        
        return dummy.next


"""This is the easy approach"""
# public ListNode removeNthFromEnd(ListNode head, int n) {
#     ListNode dummy = new ListNode(0);
#     dummy.next = head;
#     int length  = 0;
#     ListNode first = head;
#     while (first != null) {
#         length++;
#         first = first.next;
#     }
#     length -= n;
#     first = dummy;
#     while (length > 0) {
#         length--;
#         first = first.next;
#     }
#     first.next = first.next.next;
#     return dummy.next;
# }