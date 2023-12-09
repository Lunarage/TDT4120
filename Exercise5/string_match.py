# !/usr/bin/python3
# coding=utf-8

def string_match(dna, segments):
    root = build_tree(segments)
    count = 0
    print(dna)
    print(root)
    for index in range(len(dna)):
        count += search_tree_accumulative(root, dna, index)
    print(count, '\n')
    return count


def search_tree_accumulative(root, dna, index):
    current_node = root
    count = 0
    while True:
        count += current_node.count
        if index == len(dna) or dna[index] not in current_node.children:
            return count
        current_node = current_node.children[dna[index]]
        index += 1


def build_tree(dna_sequences):
    root = Node()
    for sequence in dna_sequences:
        current_node = root
        for base in sequence:
            if base in current_node.children.keys():
                current_node = current_node.children[base]
            else:
                current_node.children[base] = Node()
                current_node = current_node.children[base]
        current_node.count += 1
    return root


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
