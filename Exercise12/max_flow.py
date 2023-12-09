#!/usr/bin/python3
# coding=utf-8


def print_flow_matrices(F, C):
    for i, k in zip(F, C):
        for j, l in zip(i, k):
            # if str(j) == "inf":
            #     print("∞".rjust(3), end=" ")
            # elif str(j) == "-inf":
            #     print("-∞".rjust(3), end=" ")
            # else:
            print(f"{j}/{l}".rjust(6), end=" ")
        print()
    print()


def max_flow(
    source: int,
    sink: int,
    nodes: List[int],
    capacities: List[List[int]]
) -> Tuple[List[List[int]], int]:

    flows = [[0] * nodes for _ in range(nodes)]
    total_flow = 0

    path = find_augmenting_path(source, sink, nodes, flows, capacities)
    while path is not None:
        flow = max_path_flow(path, flows, capacities)
        total_flow += flow
        send_flow(path, flow, flows)
        path = find_augmenting_path(source, sink, nodes, flows, capacities)

    return flows, total_flow


# Hjelpefunksjoner
def find_augmenting_path(
    source: int,
    sink: int,
    nodes: int,
    flows: List[List[int]],
    capacities: List[List[int]],
) -> Optional[List[int]]:
    """
    Finn en forøkende sti i et flytnett

    :param source: indeksen til kilden i listen med noder.
    :param sink: indeksen til sluknoden i listen med noder.
    :param nodes: antaller noder i nettverket
    :param flows: flyt-matrise, verdien på indeks (i,j) er flyten mellom node i og j
    :param capacities: kapasitets-matrise, verdien på indeks (i,j) er kapasiteten til kanten (i,j).
                        ingen kant tilsvarer kapasitet 0.
    :returns: en foreldre-liste med den flytforøkende stien hvis funnet, ellers None.
    """

    def create_path(source: int, sink: int, parent: List[int]) -> List[int]:
        """Lager en sti fra foreldrelisten"""
        node = sink
        path = [sink]
        while node != source:
            node = parent[node]
            path.append(node)
        path.reverse()
        return path

    discovered = [False] * nodes
    parent = [0] * nodes
    queue = deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        if node == sink:
            return create_path(source, sink, parent)

        for neighbour in range(nodes):
            if (
                not discovered[neighbour]
                and flows[node][neighbour] < capacities[node][neighbour]
            ):
                queue.append(neighbour)
                discovered[neighbour] = True
                parent[neighbour] = node
    return None


def max_path_flow(
    path: List[int],
    flows: List[List[int]],
    capacities: List[List[int]]
) -> int:
    """
    Finn maksimal flyt som kan sendes igjennom den oppgitte stien
    """
    flow = float("inf")
    for i in range(1, len(path)):
        u, v = path[i - 1], path[i]
        flow = min(flow, capacities[u][v] - flows[u][v])
    return flow


def send_flow(path, flow, flows):
    """
    Oppdaterer "flows" ved å sende "flow" flyt igjennom stien "path"
    """
    for i in range(1, len(path)):
        u, v = path[i - 1], path[i]
        flows[u][v] += flow
        flows[v][u] -= flow
