#!/usr/bin/python3
# coding=utf-8


def encode(data, encoding):
    out = ""
    for char in data:
        out += encoding[char]
    return out
