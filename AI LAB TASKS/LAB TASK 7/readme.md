# Quratulain 
## roll no: 156 
### section : bsai 3c
******************************
# A* Graph — README

## Purpose
Provide a compact, reusable implementation of the A* search algorithm for small weighted graphs. The script demonstrates finding a lowest-cost path between two nodes using an admissible heuristic.

## What the code does
- Defines `AStarGraph`, a helper that stores:
  - `adjacency`: mapping node -> list of (neighbor, cost)
  - `heuristic`: function node -> estimated cost to goal (defaults to zero)
- Implements `a_star(start, goal)` returning `(path_list, total_cost)` or `None` if no path exists.
- Uses a min-heap priority queue keyed by f = g + h (g = cost so far, h = heuristic).
- Reconstructs the path when the goal is reached.
- Example usage in `__main__` shows a small graph and runs A* (with zero heuristic, equivalent to Dijkstra).

## Key functions / data
- AStarGraph.__init__(adjacency, heuristic=None)
- AStarGraph.a_star(start, goal) -> Optional[Tuple[List[str], float]]
  - Returns the path and its total cost if reachable.
- Example adjacency format:
  - { "A": [("B", 1.0), ("C", 3.0)], "B": [("D", 5.0)], ... }

## Usage
1. Run the script:
   python "TASK7.PY"
2. Or import and call:
   from TASK7 import AStarGraph
   g = AStarGraph(adjacency, heuristic=h)
   path_cost = g.a_star("A", "D")

## Example output (from included demo)
Path found: ['A', 'B', 'D'] Cost: 6.0
