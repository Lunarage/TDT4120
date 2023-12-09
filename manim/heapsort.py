"""
Heapsort
"""
import math
import manim
from manim import Scene, UP, DOWN, LEFT, RIGHT, ORIGIN, VGroup


def parent(i):
    return (i+1)//2


def left(i):
    return 2*(i)+1


def right(i):
    return 2*(i)+2


class Heap(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.heap_size = len(self)-1


def ceil_to_square(n):
    return 1 if n == 0 else 2**(n-1).bit_length()


def create_tree(size):
    full_size = ceil_to_square(size) - 1
    height = math.ceil(math.log(ceil_to_square(size), 2))
    nodes = []
    nodes_vg = VGroup()
    for i in range(full_size):
        circle = manim.Circle(
            radius=0.33,
            color=manim.BLACK,
            fill_color=manim.BLACK,
            fill_opacity=1.0,
        )
        nodes.append(circle)
        nodes_vg += circle
    rows = [[] for i in range(height)]
    for index, node in enumerate(nodes):
        if index == 0:
            rows[0].append(node)
        elif index in (1, 2):
            rows[1].append(node)
        elif index in (3, 4, 5, 6):
            rows[2].append(node)
        elif index in (7, 8, 9, 10, 11, 12, 13, 14):
            rows[3].append(node)
        else:
            node_height = 0 if index == 0 else int(
                math.log(ceil_to_square(index), 2) - 1)
            rows[node_height].append(node)
    node_rows = [VGroup(*row) for row in rows]
    node_rows[-1].arrange(buff=0.75).move_to(ORIGIN).to_edge(DOWN)
    for i in range(len(rows)-2, -1, -1):
        for index, circle in enumerate(rows[i]):
            left_index = int(2*(index+2**i)-1)
            right_index = int(2*(index+2**i))
            circle.move_to(
                (
                    nodes[left_index].get_center() +
                    nodes[right_index].get_center()
                )/2
            )
            circle.shift(UP*1.5)
    return nodes, nodes_vg, node_rows


def array_to_vgroup(heap):
    """
    Make a vgroup
    """
    squares = []
    contents = []
    labels = []
    vg = manim.VGroup()
    for index, element in enumerate(heap):
        square = manim.Square(side_length=1.0)
        if index > 0:
            square.next_to(squares[index-1], manim.RIGHT, buff=0.0)
        squares.append(square)
        content = manim.Text(str(element)).scale(0.75)
        content.move_to(square)
        contents.append(content)
        label = manim.Text(str(index)).scale(0.5)
        label.next_to(square, manim.DOWN)
        labels.append(label)
        vg += square
        vg += content
        vg += label
    return vg, squares, contents


class Heapsort(Scene):
    def construct(self):
        # array = [59, 49, 76, 50, 54, 5, 4, 5, 7, 28]
        array = [5, 12, 2, 4, 8, 10, 9, 11, 6, 7, 1, 3]
        heap = Heap(array)
        self.tree, self.tree_circles, self.tree_contents = self.heap_to_tree(
            heap)
        self.array_vg, self.array_squares, self.array_contents = array_to_vgroup(
            heap)
        self.array_vg.move_to(ORIGIN).to_edge(UP)
        self.add(self.tree, self.array_vg)
        self.heapsort(heap)
        self.wait(2)

    def heap_to_tree(self, heap):
        nodes, nodes_vg, node_rows = create_tree(len(heap))
        self.add(nodes_vg)
        tree = VGroup()
        circle_list = []
        content_list = []
        node_list = []
        for index, item in enumerate(heap):
            l_index = left(index)
            r_index = right(index)
            if l_index < len(heap):
                line1 = manim.Line(
                    nodes[index].get_center(),
                    nodes[l_index].get_center()
                )
                vec1 = line1.get_unit_vector()
                line1.put_start_and_end_on(
                    nodes[index].get_center()+vec1*0.33,
                    nodes[l_index].get_center()-vec1*0.33,
                )
                tree.add(line1)
            if r_index < len(heap):
                line2 = manim.Line(
                    nodes[index].get_center(),
                    nodes[r_index].get_center()
                )
                vec2 = line2.get_unit_vector()
                line2.put_start_and_end_on(
                    nodes[index].get_center()+vec2*0.33,
                    nodes[r_index].get_center()-vec2*0.33,
                )
                tree.add(line2)
            circle = manim.Circle(
                radius=0.33,
                color=manim.WHITE,
            )
            circle.move_to(nodes[index])
            circle_list.append(circle)
            content = manim.Text(str(item), font_size=30)
            content.move_to(nodes[index])
            content_list.append(content)
            label = manim.Text(str(index), font_size=16)
            label.next_to(nodes[index], LEFT)
            tree.add(label)
            node = VGroup(circle, content)
            tree.add(node)
            node_list.append(node)
        return tree, circle_list, content_list

    def max_heapify(self, heap, index):
        lindex = left(index)
        rindex = right(index)
        if lindex <= heap.heap_size-1 and heap[lindex] > heap[index]:
            largest = lindex
        else:
            largest = index
        if rindex <= heap.heap_size-1 and heap[rindex] > heap[largest]:
            largest = rindex
        if largest != index:
            self.swap_by_index(heap, index, largest)
            self.max_heapify(heap, largest)

    def build_max_heap(self, heap, n):
        for i in range(n//2, -1, -1):
            self.max_heapify(heap, i)

    def heapsort(self, heap):
        self.build_max_heap(heap, len(heap))
        for i in range(len(heap)-1, 0, -1):
            self.swap_by_index(heap, 0, i)
            self.play(
                self.tree_circles[i].animate.set_fill(
                    manim.RED, opacity=0.50),
                self.array_squares[i].animate.set_fill(
                    manim.RED, opacity=0.50)
            )
            heap.heap_size = heap.heap_size - 1
            self.max_heapify(heap, 0)
        self.play(
            self.tree_circles[0].animate.set_fill(
                manim.RED, opacity=0.50),
            self.array_squares[0].animate.set_fill(
                manim.RED, opacity=0.50)
        )

    def swap_by_index(self, heap, i, j):
        heap[i], heap[j] = heap[j], heap[i]
        animations = [
            self.array_contents[i].animate.move_to(
                self.array_squares[j]
            ),
            self.array_contents[j].animate.move_to(
                self.array_squares[i]
            ),
            self.tree_contents[i].animate.move_to(
                self.tree_circles[j]
            ),
            self.tree_contents[j].animate.move_to(
                self.tree_circles[i]
            ),
        ]
        self.bring_to_front(self.array_contents[i])
        self.bring_to_front(self.tree_contents[j])
        self.bring_to_front(self.array_contents[j])
        self.bring_to_front(self.tree_contents[i])

        self.tree_contents[i], self.tree_contents[j] = self.tree_contents[j], self.tree_contents[i]
        self.array_contents[i], self.array_contents[j] = self.array_contents[j], self.array_contents[i]
        self.play(*animations)


def main():
    pass


if __name__ == '__main__':
    main()
