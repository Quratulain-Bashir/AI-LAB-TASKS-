from typing import Dict, List, Optional, Set

graph: Dict[str, List[str]] = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': [],
    'F': ['I', 'K'],
    'G': [],
    'H': ['L'],
    'I': [],
    'K': ['M'],
    'L': [],
    'M': []
}

def bfs(graph: Dict[str, List[str]], start: str, target: Optional[str] = None) -> List[str]:
    """
    Level-order BFS without explicit queue/Node objects.
    - Preserves adjacency order.
    - Avoids revisiting nodes (handles cycles).
    - If `target` is provided, returns early when target is found.
    """
    if start not in graph:
        raise ValueError(f"Start node {start!r} not found in graph")

    visited: List[str] = []
    seen: Set[str] = set()
    frontier: List[str] = [start]

    while frontier:
        next_frontier: List[str] = []
        for node in frontier:
            if node in seen:
                continue
            seen.add(node)
            visited.append(node)
            if target is not None and node == target:
                return visited
            # extend next frontier with children in adjacency order
            for child in graph.get(node, []):
                if child not in seen:
                    next_frontier.append(child)
        frontier = next_frontier

    return visited

if __name__ == "__main__":
    start = 'A'
    print("BFS Traversal:", bfs(graph, start))
    print("BFS until 'F':", bfs(graph, start, target='F'))
