"""
Bubblesort
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


class Bubblesort(manim.Scene):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.array = [45, 51, 48, 67, 6, 30, 29, 59, 44, 10]
        self.array_group, self.array_squares, self.array_contents = array_to_vgroup(
            self.array)
        self.marker = manim.Line()
        self.marker.set_color(manim.RED)

    def bubblesort(self, array):
        """
        The bubble sort algorithm
        """
        for i in range(len(array)):
            if i > 0:
                self.play(
                    self.marker.animate.put_start_and_end_on(self.array_squares[i].get_vertices()[
                                                             2], self.array_squares[i].get_vertices()[1] + manim.UP*0.25),
                )
            self.play(
                self.array_squares[len(array)-1].animate.set_fill(
                    manim.ORANGE, opacity=0.5),
                self.array_squares[len(array)-2].animate.set_fill(
                    manim.ORANGE, opacity=0.5),
            )
            for j in range(len(array)-1, i, -1):
                if array[j] < array[j-1]:
                    self.play(
                        self.array_contents[j].animate.move_to(
                            self.array_squares[j-1]),
                        self.array_contents[j-1].animate.move_to(
                            self.array_squares[j]),
                    )
                    self.array_contents[j], self.array_contents[j -
                                                                1] = self.array_contents[j-1], self.array_contents[j]
                    array[j], array[j-1] = array[j-1], array[j]
                if j > i+1:
                    self.play(
                        self.array_squares[j].animate.set_fill(
                            manim.ORANGE, opacity=0.0),
                        self.array_squares[j-2].animate.set_fill(
                            manim.ORANGE, opacity=0.5),
                    )
                else:
                    self.play(
                        self.array_squares[j].animate.set_fill(
                            manim.ORANGE, opacity=0.0),
                        self.array_squares[j-1].animate.set_fill(
                            manim.ORANGE, opacity=0.0),
                    )
        self.play(*[square.animate.set_fill(manim.ORANGE, opacity=0.0)
                    for square in self.array_squares],
                  manim.FadeOut(self.marker))

    def construct(self):
        # Setup
        self.add(self.array_group)
        self.array_group.move_to(manim.ORIGIN)
        self.marker.put_start_and_end_on(self.array_squares[0].get_vertices()[
                                         2], self.array_squares[0].get_vertices()[1] + manim.UP*0.25)
        self.play(manim.Create(self.marker))

        # Sort
        self.bubblesort(self.array)

        # Finish
        self.wait(2)
