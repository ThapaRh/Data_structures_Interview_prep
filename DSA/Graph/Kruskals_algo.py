#min cost to connect all the points

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
            return 0
        # We want to ensure the larger set remains the root.
        if self.size[root_A] < self.size[root_B]:
            # Make root_B the overall root.
            self.parent[root_A] = root_B
            self.size[root_B] += self.size[root_A]
            # The size of the set rooted at B is the sum of the 2.
            
        else:
            # Make root_A the overall root.
            self.parent[root_B] = root_A
            self.size[root_A] += self.size[root_B]
            # The size of the set rooted at A is the sum of the 2.
        return 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dict = {}
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                dict[(i,j)] = abs(points[j][1]-points[i][1]) + abs(points[j][0]-points[i][0])
        
        dict = sorted(dict.items(), key=lambda x:x[1])
        root = UnionFind(n)
        final = 0
        for key,value in dict:
            if root.union(key[0],key[1]) == 1:
                final+=value
                n-=1
            if n==1:
                return final
        return final

        