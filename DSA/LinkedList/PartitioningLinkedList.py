#https://www.geeksforgeeks.org/partitioning-a-linked-list-around-a-given-value-and-keeping-the-original-order/

#User function Template for python3

"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def partition(self, head, x):
        #code here
        dict={}
        dict["before"]=[]
        dict["after"]=[]
        count = 0
        while(head):
            if head.data<x:
                dict["before"].append(head.data)
            elif head.data>x:
                dict["after"].append(head.data)
            else:
                count+=1
            head= head.next
        curr = Node(-1)
        final = curr
        i=0
        while(i<len(dict["before"])):
            curr.next = Node(dict["before"][i])
            curr=curr.next
            i+=1
        while count>0:
            curr.next = Node(x)
            curr=curr.next
            count-=1
        j=0
        while(j<len(dict["after"])):
            curr.next = Node(dict["after"][j])
            curr=curr.next
            j+=1
        return final.next
        
        
        
"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""
class Solution:
    def partition(self, head, x):
        less = Node(-1)
        l = less
        greater = Node(-1)
        g = greater
        same = Node(-1)
        s = same
        while(head):
            if head.data<x:
                less.next = Node(head.data)
                less=less.next
            elif head.data>x:
                greater.next = Node(head.data)
                greater=greater.next
            else:
                same.next = Node(head.data)
                same = same.next
            head= head.next
        
        same.next = g.next
        less.next = s.next
        return l.next