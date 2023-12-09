# !/usr/bin/python3
# coding=utf-8


class Node:
    def __init__(self, compound):
        self.compound = compound
        self.adj = []  # (node, weight)


def initialize_single_source(G, s):
    for v in G:
        v.d = float("inf")
        v.parent = None
    s.d = 0


def relax(u, v, w):
    if v.d > u.d + w:
        v.d = u.d + w
        v.parent = u


def trace_path(u):
    path = [u.compound]
    while u.parent:
        path.insert(0, u.parent.compound)
        u = u.parent
    return path


def least_energy(reactions, start, goal, laws_of_thermodynamics=False):
    compounds = {}
    for reaction in reactions:
        comp_1, comp_2, energy = reaction
        if comp_1 not in compounds:
            compounds[comp_1] = Node(comp_1)
        if comp_2 not in compounds:
            compounds[comp_2] = Node(comp_2)
        compounds[comp_1].adj.append((compounds[comp_2], energy))
    vertices = list(compounds.values())
    initialize_single_source(vertices, compounds[start])
    for u in vertices:
        for v, w in u.adj:
            relax(u, v, w)
    path = trace_path(compounds[goal])
    return path
