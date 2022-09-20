"""
Heapsort
"""
import manim
from manim import Scene, UP, DOWN, LEFT, RIGHT, VGroup


def parent(i):
    return (i+1)//2


def left(i):
    return 2*(i+1)


def right(i):
    return 2*(i+1)+1


class Heap(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heap_size = len(self)


def max_heapify(heap, index):
    lindex = left(index)
    rindex = right(index)
    if lindex <= heap.heap_size and heap[lindex] > heap[index]:
        largest = lindex
    else:
        largest = index
    if rindex <= heap.heap_size and heap[rindex] > heap[largest]:
        largest = rindex
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        max_heapify(heap, largest)

def heap_to_tree(heap):
    tree = VGroup()
    circle_list = []
    content_list = []
    node_list = []
    for item in heap:
        circle = manim.Circle()
        circle_list.append(circle)
        content = manim.Text(str(item))
        content_list.append(content)
        node = VGroup(circle, content)
        tree.add(node)
        node_list.append(node)
    return tree, circle_list, content_list, node_list

class Heapsort(Scene):
    def construct(self):
        array = [59, 49, 76, 50, 54, 5, 4, 5, 7, 28]
        heap = Heap(array)


def main():
    array = [59, 49, 76, 50, 54, 5, 4, 5, 7, 28]
    heap = Heap(array)
    print(heap, heap.heap_size)
    max_heapify(heap, 0)
    print(heap)


if __name__ == '__main__':
    main()
