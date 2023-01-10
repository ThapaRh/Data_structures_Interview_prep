"""207. Course Schedule
Medium
12.4K
482
company
Amazon
company
Google
company
Facebook
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible."""

#TC=Time Complexity: O(∣E∣+∣V∣ where ∣V is the number of courses, and ∣E∣ is the number of dependencies. SC= Same
#TC=Time Complexity: O(∣E∣+∣V∣ where ∣V is the number of courses, and ∣E∣ is the number of dependencies. SC= Same
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict={}
        for a,b in prerequisites:
            if a not in dict:
                dict[a]=[b]
            else:
                dict[a].append(b)
            if b not in dict:
                dict[b] = []
        print(dict)
        def findCycle(val,dict,visited):
            if val in visited:
                return False
            if len(dict[val])==0:
                return True
            visited.add(val)
            for s in dict[val]:
                if findCycle(s,dict,visited)==False:
                    return False
            visited.remove(val) #after visiting we remove it from the set cause it can be visited by others as well
            dict[val]=[] #this to save time and say if empty then no loop for that

       
        for val in dict:
            if findCycle(val, dict, set())==False:
                return False
        return True
            



            

            


