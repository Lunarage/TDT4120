# !/usr/bin/python3
# coding=utf-8


def longest_decreasing_subsequence(s):
    print(f"New sequence: {s}")
    for i in range(1, len(s)+1):
        print(s[-i])
    return s
