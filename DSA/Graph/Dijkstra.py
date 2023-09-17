
import heapq
class Solution:
    def dijkstra(self,graph, start):
        # Initialize distances dictionary with infinity for all nodes except the start node.
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        
        # Create a priority queue (min-heap) to store nodes and their distances.
        priority_queue = [(0, start)]
        
        while priority_queue:
            # Pop the node with the smallest distance from the priority queue.
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node]:
                continue
            # Explore neighbors of the current node.
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                # If a shorter path is found, update the distance and push it to the priority queue.
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in range(1,n+1):
            graph[i]={}
        for time in times:
            start = time[0]
            end = time[1]
            dist = time[2]
            if start in graph:
                graph[start][end]=dist
            else:
                graph[start] = {end:dist}
        val = self.dijkstra(graph,k)
        final = 0
        for k,v in val.items():
            if v == float('inf'):
                return -1
            final = max(final,v)
        return final
            

        