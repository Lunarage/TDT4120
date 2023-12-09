# Curriculum Reference

## Topics

* Problems and algorithms
* Data structures
    * Stacks
    * Queues
    * Linked lists
    * [ Hash tables ](#hash-tables)
    * Dynamic tables
* Divide-and-conquer
    * [ Recurrences ](#recurrences)
    * Merge-sort
    * [ Quicksort ](#quicksort)
* [ Sorting in linear time ](#sorting-in-linear-time)
    * [ Counting-sort ](#counting-sort)
    * [ Radix-sort ](#radix-sort)
    * [ Bucket-sort ](#bucket-sort)
    * [ Select ](#select)
* [ Rooted trees ](#rooted-trees)
    * [ Heaps ](#heaps)
    * Heapsort
    * [ Binary search trees ](#binary-search-trees)
* [ Dynamic programming ](#dynamic-programming)
* [ Greedy algorithms ](#greedy-algorithms)
    * [ Huffman ](#huffman)
    * Gale-Shapely
* [ Elementary graph algorithms ](#elementary-graph-algorithms)
    * [ BFS ](#breath-first-search)
    * [ DFS ](#depth-first-search)
    * Topological sort
* Minimum spanning trees
    * Disjoint sets
    * Generic-MST
    * MST-Kruskal
    * MST-Prim
* [ Single source shortest paths ](#single-source-shortest-paths)
    * [ Bellman-Ford ](#bellman-ford)
    * Dag-shortest-paths
    * [ Dijkstra ](#dijkstras-algorithm)
* [ All-pairs shortest paths ](#all-pairs-shortest-paths)
    * Slow-APSP
    * Faster-APSP
    * Floyd-Warshall
    * Transitive-Closure
    * Johnson
* [ Matching in bipartite graphs ](#matching-in-bipartite-graphs)
* [ Maximum flow ](#maximum-flow)
    * Ford-Fulkerson
    * Edmonds-Karp
* NP Completeness

## Hash tables

### chaining
Resolve collisions in hashtables with linked lists(?).

## Recurrences

### Master theorem for solving recurrences

$T(n) = aT(n/b) + f(n)$

1. Case 1 (Harder. )  
    $\epsilon > 0$ such that $f(n) = O(n^{\log_b{a-\epsilon}})$,  
    then $T(n) = \Theta(n^{\log_b{a}})$
2. Case 2 (Equally hard)  
    $k \geq 0$ such that $f(n) = \Theta(n^{\log_b{a}}\lg^{k}n)$,  
    then $T(n) = \Theta(n^{\log_b{a}}\lg^{k+1}n)$
3. Case 3 (Easier. Driving function dominates)  
    $\epsilon > 0$ such that $f(n) = \Omega(n^{log_b{a+\epsilon}})$,  
    then $T(n) = \Theta(f(n))$

### Quicksort

```python
def exchange(A, i, j):
    """
    Swaps element at index i and element at index j in array A
    """
    A[i], A[j] = A[j], A[i]


def partition(A, p, r):
    x = A[r]  # The pivot
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            exchange(A, i, j)
    exchange(A, i+1, r)
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)
```

## Sorting in linear time

### Counting-sort

```python
def counting_sort(A, n, k):
    """
    A: list to be sorted
    n: length of list
    k: limit on values
    """
    # Create lists
    B = [None]*n
    C = [0]*k

    # Count number of elements equal to index
    for a in A:
        C[a] = C[a] + 1

    # Compute number of elements less than or equal to index
    for i in range(1, k):
        C[i] = C[i] + C[i-1]

    # Copy A to B
    for a in reversed(A):
        B[C[a]-1] = a
        # Handle duplicate values
        C[a] = C[a] - 1
    return B
```

$\Theta(n + k)$

### Radix-sort

### Bucket-sort

### Select

## Rooted trees
A rooted tree is a tree in which one vertex has been designated the root.

### Heaps

```python
def parent(i):
    return floor(i/2)

def left(i):
    return 2*i

def right(i):
    return 2*i + 1
```

The **heap property**:  
In a **max-heap**, the **max-heap property** is that for every node $i$ other than the root,
$
A[\mathrm{parent}(i)] \geq A[i]
$  
The largest element is stored at the root.

In a **min-heap**, the **min-heap property** is that for every node $i$ other than the root,
$
A[\mathrm{parent}(i)] \leq A[i]
$  
The smallest element is stored at the root.

```python
def max_heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= A.heap_size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest)
```

```python
def build_max_heap(A, n):
    A.heap_size = n
    for i in range(floor(n/2), 0, -1):
        max_heapify(A, i)
```

### Priority queues

```python
def min_heap_minimum(A):
    if A.heap_size < 1:
        raise Exception("heap underflow")
    return A[0]

def min_heap_extract_minimum(A):
    minimum = min_heap_minimum(A)
    A[0] = A[A.heap_size]
    A.heap_size -= 1
    min_heapify(A, 0)
    return minimum

```

### Binary search trees

A in binary search tree, each node has a $key$, a parent $p$, a $left$ child and a $right$ child.
The tree it self has an attribute $root$ that point to the root or NIL if the tree is empty.
The root is the only node whose parent is NIL.

Let $x$ be a node in a binary search tree.
If $y$ is a node in the left subtree of $x$, then $y.key \leq x.key$.
If $y$ is a node in the right subtree of $x$, then $y.key \geq x.key$.

```python
def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)
```

```python
def tree_search(x, k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    return tree_search(x.right, k)

def iterative_tree_search(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x
```

```python
def tree_minimum(x)
    while x.left is not None:
        x = x.left
    return x

def tree_maximum(x)
    while x.right is not None:
        x = x.right
    return x
```

```python
def tree_insert(T, z):
    x = T.root  # Node to compare
    y = None    # Parent of the new node
    while x is not None:  # Descend until reaching a leaf
        y = x
        if z.key < x.key
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is None:
        T.root = z  # Tree is empty
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
```

## Dynamic programming

### optimal substructure
A problem exhibits optimal substructure
if an optimal solution to the problem contains within it
optimal solutions to subproblems.

## Matching in bipartite graphs

**bipartite graph**  
A graph $G = (V, E)$ with vertex partition $V = L \cup R$
with no edges between vertices in $L$ and no edges between vertices in $R$.

**complete bipartite graph**  
A graph $G = (V, E)$ with vertex partition $V = L \cup R$
with no edges between vertices in $L$ and no edges between vertices in $R$
containing an edge from every vertex $L$ to every vertex in $R$.

If you know a graph is a complete bipartite graph,
then you can find a maximum matching by a simple greedy algorithm.

```
Gale-Shapely(men, women, rankings)
    Assign each man and woman as free
    while some woman _w_ is free
        let _m_ be the first man on _w_'s list to whom she has not proposed
        if _m_ is free
            _w_ and _m_ become engaged to each other (and not free)
        elif _m_ ranks _w_ higher than the woman _w'_ he is currently engaged to
            _m_ breaks the engagement to _w'_, who becomes free
            _w_ and _m_ become engaged to each other (and not free)
        else _m_ rejects _w_, with _w_ remaining free
    return the stable matching consisting of the engaged pairs
```

## Maximum flow

A __flow network__ $G=(V,E)$ is a directed graph
in with each edge $(u,v) \in E$ has a nonnegative __capacity__ $c(u,v) \geq 0$.

If $E$ contains an edge $(u,v)$, then there is no edge $(v,u)$ in the opposite direction.

Each flow network contains two distinguished vertices: a __source__ $s$ and a __sink__ $t$.

A __flow__ in $G$ is a real-valued function $f: V \times V \to \mathbb{R}$
that satisfies the following properties:

For all $u,v \in E$
$$
0 \leq f(u,v) \leq c(u,v)
$$
For all $u \in V - {s,t}$
$$
\sum_{v \in V} f(v,u) = \sum_{v \in V} f(u,v)
$$

## Elementary graph algorithms

**simple path**  
A path which does not have repeating vertices.

**sparse graph**  
A graph where $|E|$ is much less than $|V|^2$.

**dense graph**  
A graph where $|E|$ is close to $|V|^2$.


### Breath-first search

```python
def BFS(G, s):
    """
    G: a graph
    s: source vertex
    """
    for u in G.vertices - {s}:
        u.color = "WHITE"
        u.d = float("inf")
        u.parent = None
    s.color = "GRAY"
    s.d = 0
    s.parent = None
    Q = {}  # Empty queue
    enqueue(Q, s)
    while not empty(Q):
        u = dequeue(Q)
        for v in G.adj[u]:
            if v.color == "WHITE":
                v.color = "GRAY"
                v.d = u.d + 1
                v.parent = u
                enqueue(v)
        u.color = "BLACK"

```

$O(V + E)$

### Depth-first search

#### Classification of edges

1. **Tree edges** are edges discovered in the depth-first forest $G_\pi$.  
    Edge $(u,v)$ is a tree edge if $v$ was discovered first by exploring $(u,v)$.
2. **Back edges** are those edges $(u,v)$ connecting a vertex $u$ to an ancestor $v$ in a depth-first tree.  
    We consider self-loops, which may occur in directed graphs, to be back edges.
3. **Forward edges** are those nontree edges $(u,v)$ connecting a vertex $u$ to a proper descendant $v$ in a depth-first tree.
4. **Cross edges** are all other edges. They can go between vertices in the same depth-first tree,  
    as long as one vertex is not the ancestor of the other,
    or they can go between vertices in different depth-first trees.

### Topological sort

```
Topological-Sort(G)
    call DFS(G) to compute finish times v.f for each vertex v
    as each vertex finishes, insert it onto the front of a linked list
    return the linked list of vertices
```

## Greedy algorithms

### greedy-choice property
You can assemble a globally optimal solution by making locally optimal (greedy) choices.

### Huffman

```python
def huffman(C):
    """
    C: Set of characters and their frequencies
    """
    Q = C  # Min priority queue keyed on frequency of character
    for _ in range(len(C)-1):
        z = Node()
        x = Q.extract_min()
        y = Q.extract_min()
        z.left = x
        z.right = y
        z.freq = x.freq + y.freq
        Q.insert(z)
    return Q.extract_min()  # The root is the only node left
```

## Single source shortest paths

**weight function: $w: E \to \mathbb{R}$**  
**shortest-path weight: $\delta(u, v)$**

```python
def initialize_single_source(G, s):
    for v in G:
        v.d = float("inf")
        v.parent = None
    s.d = 0


def relax(u, v, w):
    if v.d < u.d + w(u, d):
        v.d = u.d + w(u, d)
        return True
    return False
```

### DAG-shortest-paths

Shortest paths single source.
No cycles (topological sort does not work with cycles)

```python
def dag_shortest_paths(G, w, s):
    """
    G: a graph
    w: weight function
    s: source
    """
    topological_sort(G)
    initialize_single_source(G, s)
    for u in G.vertices:
        for v in G.adj[u]:
            relax(u, v, w)
```

### Bellman-ford

Shortest path single source.
Returns True if and only if the graph contains no negative-weight cycles reachable from the source.

```python
def bellman-ford(G, w, s):
    """
        G: a graph
        w: weight function
        s: source vertex
    """
    initialize_single_source(G, s)
    for _ in range(len(G.vertices)):
        for u, v in G.edges:
            relax(u, v, w)
    for u, v in G.edges:
        if v.d > u.d + w(u, v)
            return False
    return True
```

### Dijkstra's algorithm

Shortest path single source. No negative edges or cycles.

```python
def dijkstra(G, w, s):
    """
    G: a graph
    w: weight function
    s: source vertex
    """
    initialize_single_source(G, s)
    S = {} # Empty set
    Q = {} # Empty min-priority queue
    for u in G.vertices:
        Q.insert(u)
    while not Q.empty():
        u = extract_min(Q)
        S = S.union({u})
        for v in G.adj[u]:
            if relax(u, v, w):
                Q.decrease_key(v, v.d)
```

## All-pairs shortest paths

### Slow-ASPS

```python
def extend_shortest_paths(L_0, W, L_1, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                L_1[i][j] = min(L_1[i][j], L_0[i][k] + W[k][j])


def slow_apsp(W, L_0, n):
    INF = float("inf")
    L = L_0[::]
    for r in range(1, n):
        M = [[INF for _ in range(n)] for _ in range(n)]
        extend_shortest_paths(L, W, M, n)
        L = M[::]
        print(r)
        print_matrix(L)
    return L
```