# """
# Two ways to represent: Adjacency List 
# Adjacency Matrix 
# """
# graph = {
#     'a': ['b','c'],
#     'b': ['d'],
#     'c':[],
#     'd':['f'],
#     'e':[],
#     'f':[],
# }

# #check to see if there is a path from one node to another DFS recursive
# visited=set()
# def DFS(graph,a,target):
#     if a==target:
#         return True
#     if a in visited:
#         return False
#     for val in graph[a]:
#         if DFS(graph,val,target):
#             return True
    
#     return False

# print(DFS(graph,'a','f'))
# print(DFS(graph,'a','e'))

# #check to see if there is a path from one node to another DFS stack

# def DFStack(graph,a,target):
#     new_visited=set()
#     stack=[]
#     stack.append(a)
#     while len(stack)!=0:
#         val = stack.pop()
#         if val in new_visited:
#             break
#         new_visited.add(val)
#         for nodes in graph[val]:
#             if nodes==target:
#                 return True
#             stack.append(nodes)
    
#     return False

# print(DFStack(graph,'a','f'))
# print(DFS(graph,'a','e'))

# #///////////////////////////////////////////////////////////////////////////////////
# #BFS uses queue

# def BFS(graph,a):
#     queue = []
#     queue.append(a)
#     visited=set()
#     while(len(queue)!=0):
#         val = queue.pop(0)
#         if val in visited:
#             break
#         print(val)
#         for nodes in graph[val]:
#             queue.append(nodes)
# BFS(graph,"a")

# def solution(inputStr):
#     def countSolution(inputStr):
#         n=len(inputStr)
#         res = 0 
#         count = [0 for i in range(26)]
#         for i in range(n):
#             count[ord(inputStr[i]) - ord('a')]-=1
#         for i in range(26):
#             if count[i]%2==1:
#                 res-=1
            
#             if res==0:
#                 return 0
#             else:
#                 return res-1
    
#     count = countSolution(inputStr)
#     if count==0 and len(inputStr)%2==0:
#         return 27
#     elif count==0 and len(inputStr)%2!=0:
#         return 1
#     else:
#         return count

# def f(n):
#     if n==1:
#         return n
#     return f(n-1) - f(n-2)

# print(f(9))

# def solution(inputStr):
#     def countSolution(inputStr):
#         dict = {}
#         count=0
#         for letters in inputStr:
#             if letters in dict:
#                 dict[letters]-=1
#             else:
#                 dict[letters]=1
#         for letters in dict:
#             if dict[letters] %2 == 1:
#                 count-=1
#         if count==0:
#             return 27
#         elif count==1:
#             return 1
#         elif count==2:
#             return 2
#         else:
#             return 0
# print(solution("aabb"))

def run_service(s , d , p):
    n = len(s)
    task = []
    for i in range(n):
        task.append(i)
    for j in range(1,n):
        if(p[j] < p[j - 1]):
            task[j] , task[j - 1] = task[j - 1] , task[j]
        elif(p[j] == p[j - 1]):
            if(s[j] > s[j - 1]):
                task[j] , task[j - 1] = task[j - 1] , task[j]
            elif(s[j] == s[j - 1]):
                if(d[j] > d[j - 1]):
                    task[j] , task[j - 1] = task[j - 1] , task[j]
                elif(d[j] == d[j - 1]):
                    if(task[j] > task[j - 1]):
                        task[j] , task[j - 1] = task[j - 1] , task[j]
            
    return task

s = [0 , 2 , 2, 0]
d = [1 , 1 , 1, 1]
p = [0 , 0 , 1, 1]
print(run_service(s , d , p))
