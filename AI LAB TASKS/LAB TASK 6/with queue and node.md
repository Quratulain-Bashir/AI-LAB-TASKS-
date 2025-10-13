# Quratulain 
## roll no: 156 
### section : bsai 3c
******************************
# BFS with Queue & Node — README

## Purpose
Small demonstration script that performs breadth-first search (BFS) on a simple adjacency graph using a queue of Node objects. Intended for learning BFS traversal and how to manage visited/state tracking.

## What the code does
- Defines a lightweight `Node` class that wraps a state string.
- Stores a directed adjacency `graph` mapping node state -> list of child state strings.
- Implements `bfs_with_queue(start, graph, target=None)`:
  - Uses a deque of `Node` objects to traverse the graph in BFS order.
  - Tracks visited states to avoid revisiting.
  - Optionally stops early if `target` is found.
- When run as a script, it prints BFS traversal from a hard-coded start node and an example early-stop run.

## Usage
1. Open a terminal (PowerShell / CMD) in the script folder.
2. Run:
   ```
   python "with queueu and node.py"
   ```
3. Inspect printed BFS orders. Modify `start`, `graph`, or call `bfs_with_queue` from other code.

## Example output
BFS with (Queue & Node): ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M']  
BFS until 'F': ['A', 'B', 'C', 'D', 'E', 'F']

## Notes & extensions
- The graph is static and encoded as an adjacency dict; swap for dynamic input or file loading as needed.
- Extend to return paths, handle weights, or convert `Node` to hold parent pointers for reconstructing routes.
- Suitable for educational purposes and simple BFS-based search tasks.
```// filepath: c:\Users\HAROON-CHISHTI\Desktop\ANIEE\aI LAB TASKS '\LAB TASK 6\README.md

# BFS with Queue & Node — README

## Purpose
Small demonstration script that performs breadth-first search (BFS) on a simple adjacency graph using a queue of Node objects. Intended for learning BFS traversal and how to manage visited/state tracking.

## What the code does
- Defines a lightweight `Node` class that wraps a state string.
- Stores a directed adjacency `graph` mapping node state -> list of child state strings.
- Implements `bfs_with_queue(start, graph, target=None)`:
  - Uses a deque of `Node` objects to traverse the graph in BFS order.
  - Tracks visited states to avoid revisiting.
  - Optionally stops early if `target` is found.
- When run as a script, it prints BFS traversal from a hard-coded start node and an example early-stop run.

## Usage
1. Open a terminal (PowerShell / CMD) in the script folder.
2. Run:
   ```
   python "with queueu and node.py"
   ```
3. Inspect printed BFS orders. Modify `start`, `graph`, or call `bfs_with_queue` from other code.

## Example output
BFS with (Queue & Node): ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M']  
BFS until 'F': ['A', 'B', 'C', 'D', 'E', 'F']

## Notes & extensions
- The graph is static and encoded as an adjacency dict; swap for dynamic input or file loading as needed.
- Extend to return paths, handle weights, or convert `Node` to hold parent pointers for reconstructing routes.
- Suitable for educational purposes and simple BFS-based search tasks.