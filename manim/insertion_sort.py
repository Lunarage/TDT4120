"""
Insertion Sort
"""
import manim


def array_to_vgroup(array):
    """
    Make a vgroup
    """
    squares = []
    contents = []
    vg = manim.VGroup()
    for index, element in enumerate(array):
        square = manim.Square(side_length=1.0)
        if index > 0:
            square.next_to(squares[index-1], manim.RIGHT, buff=0.0)
        squares.append(square)
        content = manim.Text(str(element)).scale(0.75)
        content.move_to(square)
        contents.append(content)
        vg += square
        vg += content
    return vg, squares, contents


class InsertionSort(manim.Scene):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.array = [5, 1, 7, 32, 8, 3, 8, 2, 4, 67]
        self.array_group, self.array_squares, self.array_contents = array_to_vgroup(
            self.array)

    def insertion_sort(self, array):
        """
        The algorithm
        """
        for i in range(len(array)):
            key_content = self.array_contents[i]
            self.play(key_content.animate.move_to(manim.ORIGIN+manim.DOWN))
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                self.array_contents[j+1] = self.array_contents[j]
                self.play(self.array_contents[j].animate.move_to(self.array_squares[j+1]))
                array[j+1] = array[j]
                j = j - 1
            self.play(key_content.animate.move_to(self.array_squares[j+1]))
            self.array_contents[j+1] = key_content
            array[j+1] = key

    def construct(self):
        """
        Main procedure
        """

        self.add(self.array_group)
        self.array_group.move_to(manim.ORIGIN)
        self.play(self.array_group.animate.move_to(manim.ORIGIN + manim.UP))
        self.insertion_sort(self.array)
        self.play(self.array_group.animate.move_to(manim.ORIGIN))
        self.wait(2)
