"""
    Find the biggest value in a unimodal list
"""


def find_maximum(x):
    return _find_maximum(x, 0, len(x)-1)


def _find_maximum(x, l, r):
    # Base case
    if r-l < 2:
        # Two or fewer elements
        return max(x[l], x[r])

    # Left is maximum
    if x[l-1] < x[l] > x[l+1]:
        return x[l]

    # Centre index
    c = (l + r) // 2

    # Increasing at l
    if x[l-1] < x[l] < x[l+1]:
        # Increasing at c and c > l
        if x[c] < x[c + 1] and x[c] > x[l]:
            # Right
            return _find_maximum(x, c, r)
        # Left
        return _find_maximum(x, l, c)

    if x[c] < x[l] or x[c] < x[c+1]:
        # Right
        return _find_maximum(x, c, r)

    # Left
    return _find_maximum(x, l, c)
