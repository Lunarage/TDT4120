"""
Animation of quicksort
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


class Quicksort(manim.Scene):
    """
    Scene rendering quicksort
    """

    def swap_by_index(self, i, j, array):
        self.play(
            self.array_contents[i].animate.move_to(
                self.array_contents[j]
            ),
            self.array_squares[j].animate.set_fill(
                manim.BLUE, opacity=0.5
            ),
            self.array_contents[j].animate.move_to(
                self.array_contents[i]
            ),
            self.array_squares[i].animate.set_fill(
                manim.ORANGE, opacity=0.5
            ),
        )
        self.array_contents[i], self.array_contents[j] = self.array_contents[j], self.array_contents[i]
        array[i], array[j] = array[j], array[i]

    def compare(self, left, right, comparison):
        vg = manim.VGroup()
        comparison_label = manim.Text(str(comparison)).to_edge(manim.UP)
        left_label = manim.Text(str(left)).next_to(
            comparison_label, manim.LEFT)
        right_label = manim.Text(str(right)).next_to(
            comparison_label, manim.RIGHT)
        vg += comparison_label
        vg += left_label
        vg += right_label
        self.play(
            manim.Create(comparison_label),
            manim.Create(left_label),
            manim.Create(right_label),
        )
        return vg

    def partition(self, array, p, pivot_index):
        # Setup
        pivot_element = array[pivot_index]
        i = p-1  # Highest index on low side
        animations = [
            self.array_squares[pivot_index].animate.set_fill(
                manim.YELLOW, opacity=0.5
            ),
            self.r_marker.animate.next_to(
                self.array_squares[pivot_index], manim.UP
            ),
            self.j_marker.animate.next_to(
                self.array_squares[0], manim.UP+manim.LEFT
            ),
            self.p_marker.animate.next_to(
                self.array_squares[p], manim.DOWN, buff=0.5
            ),
        ]
        if i < 0:
            animations += [
                self.i_marker.animate.next_to(
                    self.array_squares[0], manim.LEFT
                )]
        else:
            animations += [
                self.i_marker.animate.next_to(
                    self.array_squares[i], manim.UP
                )]
        self.play(*animations)

        # Main loop
        for j in range(p, pivot_index):
            self.play(self.j_marker.animate.next_to(
                self.array_squares[j], manim.UP)
            )
            if array[j] > pivot_element:
                comparison = self.compare(array[j], pivot_element, ">")
                self.play(
                    self.array_squares[j].animate.set_fill(
                        manim.BLUE, opacity=0.5
                    ),
                )
                self.play(manim.FadeOut(comparison))
            if array[j] <= pivot_element:
                comparison = self.compare(array[j], pivot_element, "≤")
                i = i + 1
                self.play(
                    self.i_marker.animate.next_to(
                        self.array_squares[i], manim.UP),
                    self.array_squares[i].animate.set_fill(
                        manim.ORANGE, opacity=0.5),
                )
                if i != j:
                    self.swap_by_index(i, j, array)
                self.play(manim.FadeOut(comparison))
        # Move pivot element
        if i+1 != pivot_index:
            self.play(
                self.array_contents[i+1].animate.move_to(
                    self.array_contents[pivot_index]),
                self.array_contents[pivot_index].animate.move_to(
                    self.array_contents[i+1]),
            )
            self.array_contents[i+1], self.array_contents[pivot_index] = self.array_contents[pivot_index], self.array_contents[i+1]
            array[i+1], array[pivot_index] = array[pivot_index], array[i+1]

        # Reset square colors
        self.play(
            *[square.animate.set_fill(manim.YELLOW, opacity=0.0)
              for square in self.array_squares]
        )
        # return partition index
        return i + 1

    def quicksort(self, array, p, r):
        if p < r:
            q = self.partition(array, p, r)
            self.quicksort(array, p, q-1)
            self.quicksort(array, q+1, r)

    def construct(self):
        array = [2, 8, 7, 1, 3, 5, 6, 4]

        self.array_group, self.array_squares, self.array_contents = array_to_vgroup(
            array)
        self.array_group.move_to(manim.ORIGIN)
        self.add(self.array_group)
        self.j_marker = manim.Text("j").scale(
            0.75).next_to(self.array_squares[0], manim.UP+manim.LEFT)
        self.i_marker = manim.Text("i").scale(
            0.75).next_to(self.array_squares[0], manim.LEFT)
        self.p_marker = manim.Text("p").scale(0.75).next_to(
            self.array_squares[0], manim.DOWN, buff=0.5)
        self.r_marker = manim.Text("r").scale(
            0.75).next_to(self.array_squares[-1], manim.UP)
        self.add(self.j_marker)
        self.add(self.i_marker)
        self.add(self.p_marker)
        self.add(self.r_marker)

        self.quicksort(array, 0, len(array)-1)
        self.play(
            manim.FadeOut(self.j_marker),
            manim.FadeOut(self.i_marker),
            manim.FadeOut(self.p_marker),
            manim.FadeOut(self.r_marker),
        )
        self.wait(2)
