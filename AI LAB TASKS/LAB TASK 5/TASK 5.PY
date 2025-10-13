from __future__ import annotations
from dataclasses import dataclass, field
from collections import deque
from typing import Dict, List, Iterable, Iterator, Optional, Set, Sequence

@dataclass
class GraphNode:
    key: int
    neighbors: List["GraphNode"] = field(default_factory=list)

def build_graph(adj: Dict[int, Sequence[int]]) -> Dict[int, GraphNode]:
    """
    Build GraphNode objects for adjacency mapping.
    Ensures nodes exist for keys referenced only as neighbors.
    """
    nodes: Dict[int, GraphNode] = {}
    for u in adj:
        nodes.setdefault(u, GraphNode(u))
    for u, vs in adj.items():
        u_node = nodes[u]
        for v in vs:
            v_node = nodes.setdefault(v, GraphNode(v))
            u_node.neighbors.append(v_node)
    return nodes

def dfs_stack(nodes: Dict[int, GraphNode], start_key: int) -> List[int]:
    """Iterative DFS using explicit stack. Returns visitation order."""
    if start_key not in nodes:
        return []
    visited: Set[int] = set()
    order: List[int] = []
    stack: List[GraphNode] = [nodes[start_key]]
    while stack:
        node = stack.pop()
        if node.key in visited:
            continue
        visited.add(node.key)
        order.append(node.key)
        # push neighbors in reverse so the original order is preserved
        for nb in reversed(node.neighbors):
            if nb.key not in visited:
                stack.append(nb)
    return order

def bfs(nodes: Dict[int, GraphNode], start_key: int) -> List[int]:
    """Breadth-first traversal from start_key."""
    if start_key not in nodes:
        return []
    visited: Set[int] = set([start_key])
    order: List[int] = []
    q: deque[GraphNode] = deque([nodes[start_key]])
    while q:
        node = q.popleft()
        order.append(node.key)
        for nb in node.neighbors:
            if nb.key not in visited:
                visited.add(nb.key)
                q.append(nb)
    return order

@dataclass
class TNode:
    val: int
    left: Optional["TNode"] = None
    right: Optional["TNode"] = None

# Tree traversal generators (iterative)
def preorder_gen(root: Optional[TNode]) -> Iterator[int]:
    if not root:
        return
        yield  # type: ignore[unreachable]
    stack: List[TNode] = [root]
    while stack:
        node = stack.pop()
        yield node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def inorder_gen(root: Optional[TNode]) -> Iterator[int]:
    stack: List[TNode] = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        yield cur.val
        cur = cur.right

def postorder_gen(root: Optional[TNode]) -> Iterator[int]:
    if not root:
        return
        yield  # type: ignore[unreachable]
    stack: List[TNode] = []
    last_visited: Optional[TNode] = None
    cur: Optional[TNode] = root
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            peek = stack[-1]
            if peek.right and last_visited is not peek.right:
                cur = peek.right
            else:
                yield peek.val
                last_visited = stack.pop()

# Convenience wrappers returning lists (compatible with previous interface)
def preorder_iter(root: Optional[TNode]) -> List[int]:
    return list(preorder_gen(root))

def inorder_iter(root: Optional[TNode]) -> List[int]:
    return list(inorder_gen(root))

def postorder_iter(root: Optional[TNode]) -> List[int]:
    return list(postorder_gen(root))

# Simple demonstration when executed as a script
if __name__ == "__main__":
    adj = {0: [1, 2], 1: [2, 3], 2: [3], 3: [1, 4], 4: []}
    nodes = build_graph(adj)
    print("DFS (stack) order:", dfs_stack(nodes, 0))
    print("BFS order:", bfs(nodes, 0))

    root = TNode(1,
                 TNode(2, TNode(4), TNode(5)),
                 TNode(3, TNode(6), TNode(7)))
    print("Preorder:", preorder_iter(root))
    print("Inorder :", inorder_iter(root))
    print("Postorder:", postorder_iter(root))