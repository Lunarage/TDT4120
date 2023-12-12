# Curriculum Reference

## Topics

* Problems and algorithms
* [ Data structures ](#data-structures)
    * Stacks
    * Queues
    * Linked lists
    * [ Hash tables ](#hash-tables)
    * Dynamic tables
* [ Divide-and-conquer ](#divide-and-conquer)
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
* [ Elementary graph algorithms ](#elementary-graph-algorithms)
    * [ BFS ](#breath-first-search)
    * [ DFS ](#depth-first-search)
    * [ Topological sort ](#topological-sort)
* [ Minimum spanning trees ](#minimum-spanning-trees)
    * Disjoint sets
    * Generic-MST
    * [ MST-Kruskal ](#kruskal)
    * MST-Prim
* [ Single source shortest paths ](#single-source-shortest-paths)
    * [ Bellman-Ford ](#bellman-ford)
    * [ Dag-shortest-paths ](#dag-shortest-paths)
    * [ Dijkstra ](#dijkstras-algorithm)
* [ All-pairs shortest paths ](#all-pairs-shortest-paths)
    * [ Slow-APSP ](#slow-asps)
    * Faster-APSP
    * [ Floyd-Warshall ](#floyd-warshall)
    * [ Transitive-Closure ](#transitive-closure)
    * Johnson
* [ Matching in bipartite graphs ](#matching-in-bipartite-graphs)
    * [ Gale Shapely ](#gale-shapely)
* [ Maximum flow ](#maximum-flow)
    * [ Ford-Fulkerson ](#ford-fulkerson-method)
    * [ Edmonds-Karp ](#edmonds-karp)
* NP Completeness

## Data structures

### Hash tables

#### chaining
Resolve collisions in hashtables with linked lists(?).

## Divide-and-conquer
### Recurrences

#### Master theorem for solving recurrences

$T(n) = aT(n/b) + f(n)$

1. Case 1 (Harder. Recurrence dominates)  
    $\epsilon > 0$ such that $f(n) = O(n^{\log_b{a-\epsilon}})$,  
    then $T(n) = \Theta(n^{\log_b{a}})$
2. Case 2 (Equally hard)  
    $k \geq 0$ such that $f(n) = \Theta(n^{\log_b{a}}\lg^{k}n)$,  
    then $T(n) = \Theta(n^{\log_b{a}}\lg^{k+1}n)$
3. Case 3 (Easier. Driving function dominates)  
    $\epsilon > 0$ such that $f(n) = \Omega(n^{log_b{a+\epsilon}})$,  
    then $T(n) = \Theta(f(n))$

### Merge sort

```python
def merge(array, first, mid, last):
    """
    Merges two sorted subarrays
    """
    # Splice it right in two
    left = array[first:mid+1]
    right = array[mid+1:last+1]
    # Iterator variables
    i = 0
    j = 0
    k = first
    # Main loop
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    # Remaining elements
    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(array, first, last):
    """
    The main sorting alogrithm
    """
    if first >= last:
        return
    mid = (first+last)//2
    merge_sort(array, first, mid)
    merge_sort(array, mid+1, last)
    merge(array, first, mid, last)
```

Average running time: $O(n \lg n)$  
Worst case running time: $O(n^2)$ (when list is sorted)  

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

Recursively partition the list.
Partition collects all values lower than the pivot (and the pivot it self) on the left.

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

    # Copy A to B (reversed to make the algorithm stable)
    for a in reversed(A):
        B[C[a]-1] = a
        # Handle duplicate values
        C[a] = C[a] - 1
    return B
```

$\Theta(n + k)$

Count the number of integers in the list, A, equal to position i C.
Modify C to be the number of integers less than or equal to the position.
For each element in A, place it in B at the position it occurs in C.

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

Find largest of the two children who is larger than the parent.
If so, change the places of the parent and the larger child.
Repeat until the parent is largest.

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

Insert node as leaf. Go left if node is lower, right if higher.

## Dynamic programming

### optimal substructure
A problem exhibits optimal substructure
if an optimal solution to the problem contains within it
optimal solutions to subproblems.

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

Create a node with frequency as the sum of the frequencies of the two nodes with the lowest frequencies.
The two nodes are children of the new node.
The node with the lowest frequency of the two is the left child and the other is the right child.
Repeat until all nodes are in the tree.
Left is "0" and right is "1".

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

Running time: $O(V + E)$

Starting with the source vertex, each vertex reachable from a discovered vertex is added to a queue, marked with "GREY" and the discovery time is noted. When all edges from a vertex have been processed, the vertex is marked "BLACK"

### Depth-first search

```python
def DFS(G):
    for v in G.vertices:
        v.color = "WHITE"
        v.parent = None
    time = 0
    for v in G.vertices:
        if u.color = "WHITE"
            DFS_Visit(G, u)

def DFS_Visit(G, u):
    time += 1
    u.d = time
    u.color = "GRAY"
    for v in G.adj[u]:
        if v.color = "WHITE":
            v.parent = u
            DFS_Visit(G, v)
    time += 1
    u.f = time
    u.color = "BLACK"
```


#### Classification of edges

1. **Tree edges** are edges discovered in the depth-first forest $G_\pi$.  
    Edge $(u,v)$ is a tree edge if $v$ was discovered first by exploring $(u,v)$.
2. **Back edges** are those edges $(u,v)$ connecting a vertex $u$ to an ancestor $v$ in a depth-first tree.  
    We consider self-loops, which may occur in directed graphs, to be back edges.
3. **Forward edges** are those non-tree edges $(u,v)$ connecting a vertex $u$ to a proper descendant $v$ in a depth-first tree.
4. **Cross edges** are all other edges. They can go between vertices in the same depth-first tree,  
    as long as one vertex is not the ancestor of the other,
    or they can go between vertices in different depth-first trees.

### Topological sort

Sorts vertices descending on finish time

```
Topological-Sort(G)
    call DFS(G) to compute finish times v.f for each vertex v
    as each vertex finishes, insert it onto the front of a linked list
    return the linked list of vertices
```

## Minimum Spanning Trees

A **cut** $(S, V-S)$ of an undirected graph $G = (V,E)$ is a partition of $V$.  
We say that an edge $(u,v) \in E$ **crosses** the cut $(S, V-S)$ if one endpoint belongs to $S$ and the other belongs to $V-S$.  
A cut **respects** a set $A$ of edges if no edge in $A$ crosses the cut.  
An edge is a **light edge** crossing a cut if its weight is the minimum of any edge crossing the cut.

> Let $G=(V,E)$ be a connected, undirected graph with a real-valued weight function $w$ defined on $E$.  
> Let $A$ be a subset of $E$ that is included in some minimum spanning tree for $G$,  
> let $(S, V - S)$ be any cut of $G$ that respects $A$,  
> and let $(u,v)$ be a light edge crossing (S, S-V).  
> Then, edge $(u,v)$ is safe for $A$.  

### Kruskal

```python
def mst_kruskal(G, w):
    A = {}
    for v in G.vertices:
        {v}
    edges = G.edges
    edges = sorted(edges)  # Sort edges ascending on weight
    for edge in edges:
        u, v = edge
        if find_set(u) != find_set(v):
            A = A.union(edge)
            union(u,v)
    return A
```

For all edges, sorted ascending by weight, add edge to tree if the vertices the edge connect does not belong to the same tree.

### Prim

```python
def mst_prim(G, w, r):
    """
        G: A connected undirected graph
        w: weight function
        r: starting vertex
    """
    # Initialize
    for v in G.vertices:
        v.key = float("inf")
        v.parent = None
    r.key = 0
    # Min-priority queue containing vertices not in tree
    Q = {} 
    for v in G.vertices:
        Q.insert(v)
    while not Q.empty():
        u = Q.extract_min()
        for v in G.adj[u]:
            if v in Q and w(u,v) < v.key
                v.parent = u
                v.key = w(u,v)
                Q.decrease_key(v, w(u, v))
```

Consider the cut that separates the tree and the rest of the graph. Add the light weight crossing the cut to the tree.


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

For all edges in the graph, taken i topological order, relax adjacent edges.

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

For all vertices relax all edges.
Check all edges again. If any edges can be relaxed, there is a negative cycle.

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

Running time depends on implementation of min-queue:  
Array: $O(V^2 + E) = O(V^2)$  
Binary min-heap: $O((V+E) \lg V) = O(E \lg V)$

Check adjacencies of the vertex with the current lowest distance estimate.

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
    return L
```

### Floyd-Warshall

```python
def floyd_warshall(W, n):
    D = [W]
    for k in range(n):
        D.append([[float("inf") for _ in range(n)] for _ in range(n)])
        for i in range(n):
            for j in range(n):
                D[k+1][i][j] = min(D[k][i][j], D[k-1][i][k] + D[k][k][j])
    return D[n]
```

From vertex _i_ to _j_, check if distance _ik_ + _kj_ is greater than self distance.
Is the distance shorter via _k_?

#### Constructing a shortest path

$$
\pi^{(0)}_{ij} =
\begin{cases}
    NIL & \text{if}\: i = j \: \text{or} \: w_{ij} = \infty \\
    i & \text{if}\: i \neq j \: \text{and} \: w_{ij} < \infty 
\end{cases}
$$

$$
\pi^{(k)}_{ij} =
\begin{cases}
    \pi^{(k-1)}_{kj} & \text{if}\: d^{(k-1)}_{ij} > d^{(k-1)}_{ik} +  d^{(k-1)}_{kj} \\
    \pi^{(k-1)}_{ij} & \text{if}\: d^{(k-1)}_{ij} \leq d^{(k-1)}_{ik} +  d^{(k-1)}_{kj} \\
\end{cases}
$$

Predecessor of _ij_ (predecessor in path from  vertex _i_ to _j_) is same as _kj_ if self distance is greater than _ik_ + _kj_,
otherwise it is same as _ij_ (it self).

### Transitive Closure

```python
def transitive_closure(G, n):
    T = [[True if j == i or (i,j) in G.edges in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = T[i][j] or (T[i][k] and T[k][j])
    return T
```

Is there a path from _i_ to _j_ or is there a path from _i_ to _j_ via _k_?

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

### Gale Shapely

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

### Ford-Fulkerson Method

```
Ford-Fulkerson-Method(G, s, t):
    initialize flow _f_ to 0
    while there exists an augmenting path _p_ in the residual network G_f
        augment flow _f_ along _p_
    return f
```

```python
def ford_fulkerson(nodes, flows, source, sink, capacities):

    # For each edge initialize flow to 0
    flows = [[0] * nodes for _ in range(nodes)]

    # Find augmenting path
    path = find_augmenting_path(s, t, nodes, flows, capacities)
    while path is not None:
        # Update flow along path
        flow = max_path_flow(path, flows, capacities)
        send_flow(path, flow, flows)
        # Find new augmenting path
        path = find_augmenting_path(source, sink, nodes, flows, capacities)

    return flows
```

### Edmonds-Karp

Ford-Fulkerson with BFS to find augmenting paths. $O(VE^2)$