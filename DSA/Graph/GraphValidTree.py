#https://leetcode.com/problems/graph-valid-tree/editorial/

#Tc = O(N) SC= O(N)
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        dict = defaultdict(list)
        if n-1!=len(edges):
            return False
        for a,b in edges:
            dict[a].append(b)
            dict[b].append(a)
        def connected(x,prev):
            if x in visited:
                return False
            visited.add(x)
            for v in dict[x]:
                if prev==v:
                    continue
                if connected(v,x)==False:
                    return False
            return True
        return connected(0,None) and n == len(visited)
    
class UnionFind:
    
    # For efficiency, we aren't using makeset, but instead initialising
    # all the sets at the same time in the constructor.
    def __init__(self, n):
        self.parent = [node for node in range(n)]
        # We use this to keep track of the size of each set.
        self.size = [1] * n
        
    # The find method, with path compression. There are ways of implementing
    # this elegantly with recursion, but the iterative version is easier for
    # most people to understand!
    def find(self, A):
        # Step 1: Find the root.
        root = A
        while root != self.parent[root]:
            root = self.parent[root]
        # Step 2: Do a second traversal, this time setting each node to point
        # directly at A as we go.
        while A != root:
            old_root = self.parent[A]
            self.parent[A] = root
            A = old_root
        return root
        
    # The union method, with optimization union by size. It returns True if a
    # merge happened, False if otherwise.
    def union(self, A, B):
        # Find the roots for A and B.
        root_A = self.find(A)
        root_B = self.find(B)
        # Check if A and B are already in the same set.
        if root_A == root_B:
            return False
        # We want to ensure the larger set remains the root.
        if self.size[root_A] < self.size[root_B]:
            # Make root_B the overall root.
            self.parent[root_A] = root_B
            # The size of the set rooted at B is the sum of the 2.
            self.size[root_B] += self.size[root_A]
        else:
            # Make root_A the overall root.
            self.parent[root_B] = root_A
            # The size of the set rooted at A is the sum of the 2.
            self.size[root_A] += self.size[root_B]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Condition 1: The graph must contain n - 1 edges.
        if len(edges) != n - 1: return False
        
        # Create a new UnionFind object with n nodes. 
        unionFind = UnionFind(n)
        
        # Add each edge. Check if a merge happened, because if it 
        # didn't, there must be a cycle.
        for A, B in edges:
            if not unionFind.union(A, B):
                return False
        
        # If we got this far, there's no cycles!
        return True    