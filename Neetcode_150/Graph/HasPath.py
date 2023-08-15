from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dicts = defaultdict(list)
        for a,b in edges:
            dicts[a].append(b)
            dicts[b].append(a)
        
        visited = set()

        def recur(a):
            if a==destination:
                return True
            if a not in visited:
                visited.add(a)
                for vals in dicts[a]:
                    if recur(vals):
                        return True
            return False
        return recur(source)


#TC = O(N)