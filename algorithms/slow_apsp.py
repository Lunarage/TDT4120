def print_matrix(M):
    for i in M:
        for j in i:
            if str(j) == "inf":
                print("∞".rjust(3), end=" ")
            else:
                print(str(j).rjust(3), end=" ")
        print()
    print()


def extend_shortest_paths(L_0, W, L_1, n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                L_1[i][j] = min(L_1[i][j], L_0[i][k] + W[k][j])


def slow_apsp(W, L_0, n):
    INF = float("inf")
    L = L_0[::]
    for r in range(1, n):
        M = [[INF for _ in range(n)] for _ in range(n)]
        extend_shortest_paths(L, W, M, n)
        L = M[::]
        print(r)
        print_matrix(L)
    return L


def main():
    INF = float("inf")
    n = 5
    W = [
        [0,    3,  8,INF, -4],
        [INF,  0,INF,  1,  7],
        [INF,  4,  0,INF,INF],
        [  2,INF, -5,  0,INF],
        [INF,INF,INF,  6,  0],
    ]
    # Matrix with 0 along the diagonal and INF else
    L_0 = [[0 if j == i else INF for j in range(n)] for i in range(n)]
    slow_apsp(W, L_0, 5)


if __name__ == "__main__":
    main()