# WITH QUEUEUE AND NODE
from collections import deque
from typing import Deque, Dict, List, Optional

class Node:
    """Lightweight Node wrapper for readability (holds a state string)."""
    def __init__(self, state: str) -> None:
        self.state = state

    def __repr__(self) -> str:
        return f"Node({self.state!r})"


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

def bfs_with_queue(start: str, graph: Dict[str, List[str]], target: Optional[str] = None) -> List[str]:
    """
    Breadth-first search using a queue of Node objects.
    Returns list of visited states in BFS order.
    If `target` is provided, stops early when target is found.
    """
    if start not in graph:
        raise ValueError(f"Start node {start!r} not found in graph")

    visited: List[str] = []
    seen: set[str] = set()
    queue: Deque[Node] = deque([Node(start)])

    while queue:
        node = queue.popleft()
        state = node.state
        if state in seen:
            continue
        seen.add(state)
        visited.append(state)
        if target is not None and state == target:
            break
        # enqueue children in the order defined by adjacency list
        for child_state in graph.get(state, []):
            if child_state not in seen:
                queue.append(Node(child_state))

    return visited

if __name__ == "__main__":
    start = 'A'
    print("BFS with (Queue & Node):", bfs_with_queue(start, graph))
    # example: stop early when target found
    print("BFS until 'F':", bfs_with_queue(start, graph, target='F'))