#!/usr/bin/python3
# coding=utf-8

import heapq


def build_decision_tree(decisions):
    nodes = []
    for decision in decisions:
        node = Node()
        node.character = decision[0]
        node.freq = decision[1]
        nodes.append(node)
    heapq.heapify(nodes)

    for _ in range(len(nodes) - 1):
        z = Node()
        x = heapq.heappop(nodes)
        y = heapq.heappop(nodes)
        z.left_child = x
        z.right_child = y
        z.freq = x.freq + y.freq
        heapq.heappush(nodes, z)

    return encoding(heapq.heappop(nodes))


def encoding(node):
    stack = [(node, "")]
    codes = {}

    while stack:
        node, code = stack.pop()

        if node.character is not None:
            codes[node.character] = code
            continue

        stack.append((node.left_child, code + "0"))
        stack.append((node.right_child, code + "1"))

    return codes


class Node:
    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.character = None
        self.freq = 0

    def __lt__(self, obj):
        return self.freq < obj.freq

    def __gt__(self, obj):
        return self.freq > obj.freq

    def __le__(self, obj):
        return self.freq <= obj.freq

    def __ge__(self, obj):
        return self.freq >= obj.freq

    def __eq__(self, obj):
        return self.freq == obj.freq
