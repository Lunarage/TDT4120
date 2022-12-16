#!/usr/bin/python3
# coding=utf-8


def encoding(node):
    codes = {}
    _encoding(node, "", codes)
    return codes

def _encoding(node, code, codes):
    if node.left_child is None and node.right_child is None:
        codes[node.character] = code
    if node.left_child is not None:
        _encoding(node.left_child, code + "0", codes)
    if node.right_child is not None:
        _encoding(node.right_child, code + "1", codes)
