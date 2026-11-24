import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # Build adjacency list
        for u, v, w in times:
            graph[u].append((v, w))

        # Min heap: (distance, node)
        min_heap = [(0, k)]

        # Track shortest distances
        dist = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)

            # Skip already visited nodes
            if node in dist:
                continue

            dist[node] = time

            # Explore neighbors
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(
                        min_heap,
                        (time + weight, neighbor)
                    )

        # Check if all nodes are reachable
        if len(dist) != n:
            return -1

        # Maximum shortest distance
        return max(dist.values())