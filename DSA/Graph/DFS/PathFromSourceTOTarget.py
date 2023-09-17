
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        final = []
        def dfs(start,end,array):
            if start == end:
                array.append(start)
                final.append(list(array))
                return
            array.append(start)
            for v in graph[start]:
                dfs(v,end,array)
                array.pop()
            return

        dfs(0,len(graph)-1,[])
        return final

"""Time Complexity: O(2^N * N)
SC = O(N)"""
# I totally don't understand where this time complexity came from