# Quratulain 
## roll no: 156 
### section : bsai 3c
******************************
# TASK 5 — Graph & Binary Tree Traversals

## Purpose
This script provides implementations and demos for common graph and binary-tree traversal algorithms. It's intended as a learning / utility module to build graphs, traverse them (DFS/BFS), and perform iterative tree traversals (preorder, inorder, postorder).

## Features
- Build a graph from an adjacency mapping into GraphNode objects (build_graph).
- Iterative graph traversals:
  - Depth-first search using an explicit stack (dfs_stack).
  - Breadth-first search using a queue (bfs).
- Binary tree node dataclass (TNode) and iterative traversal generators:
  - preorder_gen, inorder_gen, postorder_gen (each returns an iterator).
  - Convenience wrappers that return lists: preorder_iter, inorder_iter, postorder_iter.
- Safe, self-contained demo runs when executed as a script.

## Key functions (short)
- build_graph(adj: Dict[int, Sequence[int]]) -> Dict[int, GraphNode]  
  Creates GraphNode objects and links neighbors; ensures referenced nodes exist.
- dfs_stack(nodes, start_key) -> List[int]  
  Iterative DFS order from start_key.
- bfs(nodes, start_key) -> List[int]  
  Breadth-first visitation order from start_key.
- preorder_gen / inorder_gen / postorder_gen(root) -> Iterator[int]  
  Iterative generators yielding node values in the respective order.
- preorder_iter / inorder_iter / postorder_iter(root) -> List[int]  
  Return traversal results as lists.


## Example output (approx.)
DFS (stack) order: [0, 1, 2, 3, 4]  
BFS order: [0, 1, 2, 3, 4]  

Preorder: [1, 2, 4, 5, 3, 6, 7]  
Inorder : [4, 2, 5, 1, 6, 3, 7]  
Postorder: [4, 5, 2, 6, 7, 3, 1]
