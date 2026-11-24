import heapq
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int
    ) -> float:

        graph = defaultdict(list)

        # Build undirected graph
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # Max heap: (-probability, node)
        max_heap = [(-1.0, start)]

        # Maximum probability to reach each node
        prob = [0.0] * n
        prob[start] = 1.0

        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob

            # Skip outdated heap entries
            if curr_prob < prob[node]:
                continue

            # Destination reached
            if node == end:
                return curr_prob

            for neighbor, edge_prob in graph[node]:

                new_prob = curr_prob * edge_prob

                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob

                    heapq.heappush(
                        max_heap,
                        (-new_prob, neighbor)
                    )

        return 0.0