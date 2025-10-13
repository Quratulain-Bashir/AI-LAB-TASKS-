# Quratulain 
## roll no: 156 
### section : bsai 3c
******************************
# BFS — Level-order Traversal (without explicit queue/node)

Purpose
- Small educational script that performs breadth-first (level-order) traversal of a directed adjacency graph.
- Demonstrates a BFS implementation that uses frontier lists instead of an explicit queue/Node wrapper.

What the code does
- Defines a sample adjacency `graph: Dict[str, List[str]]`.
- Implements `bfs(graph, start, target=None)`:
  - Traverses nodes level-by-level.
  - Preserves adjacency order when visiting children.
  - Tracks visited nodes to avoid revisiting (handles cycles).
  - Optionally stops early when `target` is found and returns the visited order so far.
- When run as a script, it prints a full traversal from a hard-coded start node and an example early-stop traversal.

Key function
- bfs(graph, start, target=None) -> List[str]
  - Inputs:
    - graph: adjacency mapping (node -> list of neighbor nodes)
    - start: starting node key (must exist in graph)
    - target: optional node to stop early when found
  - Output: list of visited node keys in BFS order

Usage
1. Open a terminal (PowerShell / CMD).
2. Run:
   python "without queue and node.PY"
3. To reuse the function, import `bfs` and call it with your graph and start node.

Example output
BFS Traversal: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M']  
BFS until 'F': ['A', 'B', 'C', 'D', 'E', 'F']

Notes and extensions
- Frontier-list approach illustrates level-by-level processing and is simple to read.
- To reconstruct paths, modify BFS to store parent pointers.
- To handle very large graphs, consider using a deque-based queue and generators to stream results.
- The script is intended for Python 3.7+.

```// filepath: c:\Users\HAROON-CHISHTI\Desktop\AI LAB TASKS #3C\lab task 6\README.md

# BFS — Level-order Traversal (without explicit queue/node)

Purpose
- Small educational script that performs breadth-first (level-order) traversal of a directed adjacency graph.
- Demonstrates a BFS implementation that uses frontier lists instead of an explicit queue/Node wrapper.

What the code does
- Defines a sample adjacency `graph: Dict[str, List[str]]`.
- Implements `bfs(graph, start, target=None)`:
  - Traverses nodes level-by-level.
  - Preserves adjacency order when visiting children.
  - Tracks visited nodes to avoid revisiting (handles cycles).
  - Optionally stops early when `target` is found and returns the visited order so far.
- When run as a script, it prints a full traversal from a hard-coded start node and an example early-stop traversal.

Key function
- bfs(graph, start, target=None) -> List[str]
  - Inputs:
    - graph: adjacency mapping (node -> list of neighbor nodes)
    - start: starting node key (must exist in graph)
    - target: optional node to stop early when found
  - Output: list of visited node keys in BFS order

Usage
1. Open a terminal (PowerShell / CMD).
2. Run:
   python "without queue and node.PY"
3. To reuse the function, import `bfs` and call it with your graph and start node.

Example output
BFS Traversal: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M']  
BFS until 'F': ['A', 'B', 'C', 'D', 'E', 'F']

Notes and extensions
- Frontier-list approach illustrates level-by-level processing and is simple to read.
- To reconstruct paths, modify BFS to store parent pointers.
- To handle very large graphs, consider using a deque-based queue and generators to stream results.
- The script is intended for Python 3.7+.
