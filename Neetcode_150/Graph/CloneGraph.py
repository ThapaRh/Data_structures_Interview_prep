"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
"""

#if there are wuestions of making clone of doubly linked List always start off by adding that element to the dictionary. Makes it easier.

"""Time Complexity: O(N+M), where N is a number of nodes (vertices) and M is a number of edges.
Space Complexity: O(N) This space is occupied by the visited hash map and in addition to that, space would also be occupied by the recursion stack since we are adopting a recursive approach here. 
The space occupied by the recursion stack would be equal to O(H) where H is the height of the graph. Overall, the space complexity would be O(N).
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dict={}
        head=node
        if node==None:
            return None
        def clone(node):
            if node==None or node in dict:
                return 
            else:
                value=node.val
                neigh = node.neighbors
                new_node = Node(value,None)
                dict[node]=new_node
                for n in neigh:
                    clone(n)
        clone(head)
        for nodes in dict:
            for n in nodes.neighbors:
                dict[nodes].neighbors.append(dict[n])
        return dict[node]
        



            



            

            

