# !/usr/bin/python3
# coding=utf-8
import heapq


def relax(u, v, distances, t_0, t_1):
    if distances[u] <= t_0 and distances[v] > t_1:
        distances[v] = t_1
        return True
    return False


def earliest_arrival(timetable, start, goal):
    nodes = {}
    for route in timetable:
        if route[0] not in nodes:
            nodes[route[0]] = []
        if route[1] not in nodes:
            nodes[route[1]] = []
        nodes[route[0]].append(route)
    distances = {node: float("inf") for node in nodes}
    visited = {node: False for node in nodes}
    Q = []
    # Initialize Source
    distances[start] = 0
    visited[start] = True
    heapq.heappush(Q, (0, nodes[start]))
    # Main loop
    while len(Q) > 0:
        _, u = heapq.heappop(Q)
        for a, b, t_0, t_1 in u:
            if relax(a, b, distances, t_0, t_1):
                heapq.heappush(Q, (distances[b], nodes[b]))
    return distances[goal]
