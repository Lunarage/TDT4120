# !/usr/bin/python3
# coding=utf-8

def search_tree(root, dna):
    current_node = root
    for base in dna:
        if base in current_node.children.keys():
            current_node = current_node.children[base]
        else:
            return 0
    return current_node.count


class Node:
    def __init__(self):
        self.children = {}
        self.count = 0

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
