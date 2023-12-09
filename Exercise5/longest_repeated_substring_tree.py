# !/usr/bin/python3
# coding=utf-8


def longest_repeated_substring(dna, k):
    root = Node()
    longest_segment = None
    for i in range(len(dna), 0, -1):
        dna_segment = dna[i-1:len(dna)]
        current_node = root
        longest_segment = None
        for base in dna_segment:
            if base in current_node.children:
                current_node = current_node.children[base]
                current_node.count += 1
            else:
                current_node.children[base] = Node(current_node, base)
                current_node = current_node.children[base]
                current_node.count = 1

            current_sequence = current_node.find_sequence()
            if current_node.count >= k and len(current_sequence):
                longest_segment = current_node.find_sequence()
                print(longest_segment, current_node.count)
    print(root)
    return longest_segment


class Node:

    def __init__(self, parent=None, base=""):
        self.children = {}
        self.parent = parent
        self.count = 0
        self.base = base

    def __str__(self):
        representation = f"┃ count: {self.count}\n"
        r = 0
        for symbol, node in self.children.items():
            r += 1
            if r == 1:
                representation += "┃\n"
            if r != 1:
                representation += "\n"
            if r != len(self.children):
                representation += f"┣━━━┓ {symbol}"
                representation += "\n┃   " + str(node).replace("\n", "\n┃   ")
            else:
                representation += f"┗━━━┓ {symbol}"
                representation += "\n    " + str(node).replace("\n", "\n    ")
        return representation

    def find_sequence(self):
        current_node = self
        sequence = ""
        while current_node is not None:
            sequence = current_node.base + sequence
            current_node = current_node.parent
        return sequence
