# !/usr/bin/python3
# coding=utf-8


def general_floyd_warshall(D, n, f, g):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = f(D[i][j], g(D[i][k], D[k][j]))
