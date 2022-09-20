"""
Bubblesort
"""


def bubblesort(array):
    """
    The bubble sort algorithm
    """
    for i in range(len(array)):
        for j in range(len(array)-1, i, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]


def main():
    """
    The main procedure
    """
    array = [45, 51, 48, 67, 6, 30, 29, 59, 44, 10]
    print(array)
    bubblesort(array)
    print(array)


if __name__ == '__main__':
    main()
