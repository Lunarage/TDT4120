def counting_sort(A, n):
    k = 2048
    # Create lists
    B = [None]*n
    C = [0]*k

    # Count number of elements equal to index
    for a in A:
        C[a] = C[a] + 1

    # Compute number of elements less than or equal to index
    for i in range(1, k):
        C[i] = C[i] + C[i-1]

    # Copy A to B
    for a in reversed(A):
        B[C[a]-1] = a
        # Handle duplicate values
        C[a] = C[a] - 1
    return B
