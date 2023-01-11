"""There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3]."""
"""Time Complexity: O(V+E) where VVV represents the number of vertices and E represents the number of edges. Essentially we iterate through each node and each vertex in the graph once and only once.

Space Complexity: O(V+E)

We use the adjacency list to represent our graph initially. The space occupied is defined by the number of edges because for each node as the key, we have all its adjacent nodes in the form of a list as the value. Hence, O(V)

Additionally, we apply recursion in our algorithm, which in worst case will incur O(E) extra space in the function call stack.

To sum up, the overall space complexity is O(V+E)"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dict = {c:[] for c in range(numCourses)} #because there is distinct number of courses given as n
        visited=set()
        cycle=set()
        finalArray=[]
        for a,b in prerequisites:
            dict[a].append(b)
        def recur(val):
            if val in visited:
                return True
            if val in cycle:
                return False
            if len(dict[val])==0:
                visited.add(val)
                finalArray.append(val)
                return True
            cycle.add(val)
            for values in dict[val]:
                if recur(values)==False:
                    return False
            finalArray.append(val)
            cycle.remove(val)
            visited.add(val)
            return True




        for val in dict:
            if val in visited:
                continue
            if recur(val)==False:
                return []
        return finalArray


