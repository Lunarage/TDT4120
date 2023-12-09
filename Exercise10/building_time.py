# !/usr/bin/python3
# coding=utf-8


def DFS_topological_sort(G):
    for task in G:
        task.color = "WHITE"
        task.parent = None
    topological_sorted_list = []
    time = [0]

    def DFS_visit(G, u):
        time[0] += 1
        u.d = time[0]
        u.color = "GRAY"
        for v in u.depends_on:
            if v.color == "WHITE":
                v.parent = u
                DFS_visit(G, v)
        time[0] += 1
        u.f = time[0]
        u.color = "BLACK"
        topological_sorted_list.insert(0, u)

    for u in G:
        if u.color == "WHITE":
            DFS_visit(G, u)
    return topological_sorted_list


def initialize_single_source(G, s):
    for v in G:
        v.d = v.time
        v.parent = None


def relax(u, v, w):
    if v.d < u.d + w:
        v.d = u.d + w
        v.parent = u


def building_time(tasks):
    initialize_single_source(tasks, tasks[0])
    for u in tasks:
        for v in u.depends_on:
            relax(u, v, v.time)
    time_list = [0]*len(tasks)
    for task in tasks:
        time_list[task.i] = task.d
    return (max(time_list))


class Task:
    def __init__(self, time, depends_on, i):
        self.time = time
        self.depends_on = depends_on
        self.i = i

    def __str__(self):
        depends_on_str = ", ".join(
            "Task " + str(task.i) for task in self.depends_on
        )
        return "Task {:}: {{time: {:}, depends_on: ".format(
            self.i, self.time
        ) + "[{:}]}}".format(depends_on_str)

    def __repr__(self):
        return str(self)
