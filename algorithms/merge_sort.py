#!/usr/bin/env python
"""
Basic implementation of merge sort
"""


def merge(array, first, mid, last):
    """
    Merges two sorted subarrays
    """
    # Splice it right in two
    left = array[first:mid+1]
    right = array[mid+1:last+1]
    # Iterator variables
    i = 0
    j = 0
    k = first
    # Main loop
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    # Remaining elements
    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1


def merge_sort(array, first, last):
    """
    The main sorting alogrithm
    """
    if first >= last:
        return
    mid = (first+last)//2
    merge_sort(array, first, mid)
    merge_sort(array, mid+1, last)
    merge(array, first, mid, last)


def main():
    """
    Run the algorithm
    """
    array = [3, 50, 380, 5, 6344, 710, 6778, 24, 5, 69]
    print(array)
    merge_sort(array, 0, len(array)-1)
    print(array)


if __name__ == "__main__":
    main()
