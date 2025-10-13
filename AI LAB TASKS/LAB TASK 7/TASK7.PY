from __future__ import annotations
from typing import Dict, List, Tuple, Optional, Callable
import heapq

Adjacency = Dict[str, List[Tuple[str, float]]]
Heuristic = Callable[[str], float]


class AStarGraph:
    """
    Small A* graph helper.
    - adjacency: mapping node -> list of (neighbor, cost)
    - heuristic: function node -> estimated cost to goal (defaults to zero)
    """

    def __init__(self, adjacency: Adjacency, heuristic: Optional[Heuristic] = None) -> None:
        self.adjacency = adjacency
        self.heuristic: Heuristic = heuristic if heuristic is not None else (lambda _: 0.0)

    def a_star(self, start: str, goal: str) -> Optional[Tuple[List[str], float]]:
        """
        Run A* from `start` to `goal`.
        Returns (path_list, total_cost) if a path is found, otherwise None.
        Uses a min-heap (priority queue) keyed by f = g + h.
        """
        if start not in self.adjacency or goal not in self.adjacency:
            return None

        open_heap: List[Tuple[float, str]] = []
        heapq.heappush(open_heap, (self.heuristic(start), start))

        came_from: Dict[str, Optional[str]] = {start: None}
        g_score: Dict[str, float] = {start: 0.0}
        closed: set[str] = set()

        while open_heap:
            _, current = heapq.heappop(open_heap)
            if current in closed:
                continue
            if current == goal:
                # reconstruct path
                path: List[str] = []
                node: Optional[str] = current
                while node is not None:
                    path.append(node)
                    node = came_from[node]
                path.reverse()
                return path, g_score[current]

            closed.add(current)

            for neighbor, cost in self.adjacency.get(current, []):
                tentative_g = g_score[current] + cost
                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic(neighbor)
                    heapq.heappush(open_heap, (f, neighbor))

        return None


# Example usage
if __name__ == "__main__":
    adjacency_list: Adjacency = {
        "A": [("B", 1.0), ("C", 3.0), ("D", 7.0)],
        "B": [("D", 5.0)],
        "C": [("D", 12.0)],
        "D": [],
    }

    # simple admissible heuristic (here all zeros — reduces to Dijkstra)
    heuristic_values: Dict[str, float] = {"A": 0.0, "B": 0.0, "C": 0.0, "D": 0.0}
    def h(n: str) -> float:
        return heuristic_values.get(n, 0.0)

    graph = AStarGraph(adjacency_list, heuristic=h)
    result = graph.a_star("A", "D")
    if result is None:
        print("Path does not exist.")
    else:
        path, cost = result
        print("Path found:", path, "Cost:", cost)