#!/usr/bin/python3
# coding=utf-8


def encoding(node, code=""):
    table = {}

    def _encoding(node, code=""):
        if node.left_child is None:
            table[node.character] = code
        else:
            _encoding(node.left_child, code + "0")
            _encoding(node.right_child, code + "1")
        return

    _encoding(node)
    return table
