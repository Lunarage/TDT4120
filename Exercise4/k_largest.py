#!/usr/bin/python3
# coding=utf-8
import random


def exchange(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            exchange(A, i, j)
    exchange(A, i+1, r)
    return i + 1


def randomized_partition(A, p, r):
    i = random.randint(p, r)
    exchange(A, r, i)
    return partition(A, p, r)


def randomized_k_largest(A, p, r, i):
    if p == r:
        return A[p:]
    q = randomized_partition(A, p, r)
    if i == q:
        return A[q:]
    elif i < q:
        return randomized_k_largest(A, p, q - 1, i)
    else:
        return randomized_k_largest(A, q + 1, r, i)


def k_largest(A, n, k):
    print(A)
    if k == 0:
        return []
    print(randomized_k_largest(A, 0, n-1, n-k))
    return A
