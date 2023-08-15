from collections import defaultdict
from collections import deque

class shortestPath:
    def getShortedtPath(graph,start,end):
        q=deque()
        q.append([start,0])
        visited = set()
        while(len(q)!=0):
             top = q.popleft()
             if top[0]==end:
                 return top[1]
             for v in graph[top[0]]:
                 if v not in visited:
                     visited.add(v)
                     q.append([v,top[1]+1])
        return -1
