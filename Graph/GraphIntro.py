"""
Two ways to represent: Adjacency List 
Adjacency Matrix 
"""
graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c':[],
    'd':['f'],
    'e':[],
    'f':[],
}

#check to see if there is a path from one node to another DFS recursive
visited=set()
def DFS(graph,a,target):
    if a==target:
        return True
    if a in visited:
        return False
    for val in graph[a]:
        if DFS(graph,val,target):
            return True
    
    return False

print(DFS(graph,'a','f'))
print(DFS(graph,'a','e'))

#check to see if there is a path from one node to another DFS stack

def DFStack(graph,a,target):
    new_visited=set()
    stack=[]
    stack.append(a)
    while len(stack)!=0:
        val = stack.pop()
        if val in new_visited:
            break
        new_visited.add(val)
        for nodes in graph[val]:
            if nodes==target:
                return True
            stack.append(nodes)
    
    return False

print(DFStack(graph,'a','f'))
print(DFS(graph,'a','e'))

