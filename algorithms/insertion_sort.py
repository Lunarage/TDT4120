"""
Insertion Sort
"""


def insertion_sort(array):
    """
    The algorithm
    """
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = key


def main():
    """
    Main procedure
    """
    array = [5, 1, 7, 32, 8, 3, 8, 2, 4, 67]
    print(array)
    insertion_sort(array)
    print(array)


if __name__ == '__main__':
    main()
