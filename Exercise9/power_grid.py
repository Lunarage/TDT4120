# !/usr/bin/python3
# coding=utf-8


class Node:
    def __init__(self, substation):
        self.parent = self
        self.rank = 0
        self.pos = substation


def union(node1, node2):
    link(find_set(node2), find_set(node1))


def link(node1, node2):
    if node1.rank > node2.rank:
        node2.parent = node1
    else:
        node1.parent = node2
        if node1.rank == node2.rank:
            node2.rank += 1


def find_set(node):
    if node != node.parent:
        node.parent = find_set(node.parent)
    return node.parent


def distance(c1, c2):
    return abs(c1[0]-c2[0])+abs(c1[1]-c2[1])


def power_grid(m, n, substations):
    # Create sets
    substation_sets = []
    for substation in substations:
        substation_sets.append(Node(substation))

    # Find edges with weights
    edges = []
    for index1, substation1 in enumerate(substation_sets):
        for substation2 in substation_sets[index1+1:]:
            edges.append((substation1, substation2, distance(
                substation1.pos, substation2.pos)))
    # Sort edges by distance
    edges = sorted(edges, key=lambda edge: edge[2])

    # Minimum spanning tree
    total_distance = 0
    for edge in edges:
        if find_set(edge[0]) != find_set(edge[1]):
            total_distance += edge[2]
            union(edge[0], edge[1])
    return total_distance
