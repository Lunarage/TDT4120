"""
A simple implementation of quicksort
"""


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


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)


def main():
    array = [5, 1, 7, 32, 8, 3, 8, 2, 4, 67]
    quicksort(array, 0, 9)
    print(array)


if __name__ == "__main__":
    main()
