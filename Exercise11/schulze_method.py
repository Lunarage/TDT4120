# !/usr/bin/python3
# coding=utf-8

def print_matrix(M):
    for i in M:
        for j in i:
            if str(j) == "inf":
                print("∞".rjust(3), end=" ")
            elif str(j) == "-inf":
                print("-∞".rjust(3), end=" ")
            else:
                print(str(j).rjust(3), end=" ")
        print()
    print()


def floyd_warshall(A, n):
    D = A[::]

    def g(x, y):
        if x > 0 and y > 0:
            return min(x, y)
        return 0

    def f(x, y):
        return max(x, y)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = f(D[i][j], g(D[i][k], D[k][j]))
    return D


def schulze_method(A, n):
    for i in range(n):
        for j in range(i+1, n):
            if A[i][j] >= A[j][i]:
                A[j][i] = 0
            else:
                A[i][j] = 0

    P = floyd_warshall(A, n)
    order = []
    tally = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if P[i][j] > P[j][i]:
                tally[i] += 1
            if P[i][j] < P[j][i]:
                tally[j] += 1
    for _ in range(n):
        max_c = tally.index(max(tally))  # Strongest candidate
        tally[max_c] = float("-inf")
        order.append(max_c)

    return order
