#!/usr/bin/python3
# coding=utf-8

def char_to_int(char):
    return ord(char) - 97


def counting_sort(A, d):
    n = len(A)
    k = 26
    # Create lists
    B = [None]*n
    C = [0]*k

    # Count number of elements equal to index
    for a in A:
        char = char_to_int(a[d])
        C[char] = C[char] + 1

    # Compute number of elements less than or equal to index
    for i in range(1, k):
        C[i] = C[i] + C[i-1]

    # Copy A to B
    for a in reversed(A):
        char = char_to_int(a[d])
        B[C[char]-1] = a
        # Handle duplicate values
        C[char] = C[char] - 1
    return B


def flexradix(A, n, d):
    # Separate strings of different lengths
    print(A)
    B = [[] for _ in range(d+1)]
    for name in A:
        B[len(name)].append(name)

    C = []
    for i in range(d, 0, -1):
        C = B[i] + C
        C = counting_sort(C, i-1)
    return C
