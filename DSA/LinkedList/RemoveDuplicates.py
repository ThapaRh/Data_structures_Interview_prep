"""Given an unsorted linked list of N nodes. The task is to remove duplicate elements from this unsorted Linked List. When a value appears in multiple nodes, the node which appeared first should be kept, all others duplicates are to be removed.

Example 1:

Input:
N = 4
value[] = {5,2,2,4}
Output: 5 2 4"""

#User function Template for python3

#TC = O(n) SC= O(N)
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        if head == None:
            return None
        curr = head
        original = set()
        original.add(head.data)
        while head and head.next:
            if head.next.data in original:
                head.next = head.next.next
            else:
                original.add(head.next.data)
                head = head.next
        return curr