"""
Animation of merge sort
"""
import manim


def array_to_vgroup(array, iterator):
    """
    Make a vgroup
    """
    squares = []
    contents = []
    labels = []
    vg = manim.VGroup()
    for index, element in enumerate(array):
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
    iterator_label = manim.Text(str(iterator)).scale(
        0.5).next_to(labels[0], manim.LEFT, buff=0.5)
    vg += iterator_label
    return vg, squares, contents


class ArrayThing(manim.Scene):
    """
    A scene animating merge_sort
    """

    def replace_content(self, object_a, object_b, k):
        new_object = object_a.copy()
        self.play(new_object.animate.move_to(
            object_b), object_b.animate.fade_to(manim.ORANGE, 1.0))
        self.remove(object_b)
        self.add(new_object)

        self.array_group -= object_b
        self.array_group += new_object
        self.contents[k] = new_object

    def merge(self, array, first, mid, last):
        """
        Merges two sorted subarrays
        """
        # Splice it right in two
        left = array[first:mid+1]
        right = array[mid+1:last+1]
        self.left_group, self.left_squares, self.left_contents = array_to_vgroup(
            left, "i")
        self.right_group, self.right_squares, self.right_contents = array_to_vgroup(
            right, "j")
        self.left_group.move_to(
            self.array_squares[first], aligned_edge=manim.LEFT+manim.UP)
        self.right_group.move_to(
            self.array_squares[mid+1], aligned_edge=manim.LEFT+manim.UP)
        self.add(self.left_group, self.right_group)
        self.play(
            self.left_group.animate.move_to(
                manim.ORIGIN + manim.LEFT, aligned_edge=manim.RIGHT),
            self.right_group.animate.move_to(
                manim.ORIGIN + manim.RIGHT, aligned_edge=manim.LEFT),
        )
        # Iterator variables
        i = 0
        j = 0
        k = first
        # Light up iterator elements
        self.play(
            self.array_squares[k].animate.set_fill(
                manim.ORANGE, opacity=0.5),
            self.left_squares[i].animate.set_fill(manim.BLUE, opacity=0.5),
            self.right_squares[j].animate.set_fill(manim.RED, opacity=0.5),
            manim.Transform(self.i_counter, manim.Text(
                "i = " + str(i), color=manim.BLUE
            ).scale(0.75).move_to(self.i_counter)),
            manim.Transform(self.k_counter, manim.Text(
                "k = " + str(k), color=manim.ORANGE
            ).scale(0.75).move_to(self.k_counter)),
            manim.Transform(self.j_counter, manim.Text(
                "j = " + str(j), color=manim.RED
            ).scale(0.75).move_to(self.j_counter)),
        )
        # Main loop
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                inequality = manim.MathTex(r"\leq", font_size=102)
                inequality.shift(manim.UP*0.30)
                self.play(manim.Create(inequality))
                self.replace_content(
                    self.left_contents[i], self.contents[k], k
                )
                self.play(manim.FadeOut(inequality))
                self.remove(inequality)
                # Increment
                if i+1 < len(self.left_squares) and k+1 < len(self.array_squares):
                    self.play(
                        self.left_squares[i+1].animate.set_fill(
                            manim.BLUE, opacity=0.5),
                        self.left_squares[i].animate.set_fill(
                            manim.BLUE, opacity=0.0),
                        self.array_squares[k].animate.set_fill(
                            manim.ORANGE, opacity=0.0),
                        self.array_squares[k+1].animate.set_fill(
                            manim.ORANGE, opacity=0.5),
                        manim.Transform(self.i_counter, manim.Text(
                            "i = " + str(i+1), color=manim.BLUE
                        ).scale(0.75).move_to(self.i_counter)),
                        manim.Transform(self.k_counter, manim.Text(
                            "k = " + str(k+1), color=manim.ORANGE
                        ).scale(0.75).move_to(self.k_counter))
                    )
                elif k+1 < len(self.array_squares) and j+1 <= len(self.right_squares):
                    self.play(
                        self.left_squares[i].animate.set_fill(
                            manim.BLUE, opacity=0.0),
                        self.array_squares[k].animate.set_fill(
                            manim.ORANGE, opacity=0.0),
                        self.array_squares[k+1].animate.set_fill(
                            manim.ORANGE, opacity=0.5),
                        manim.Transform(self.k_counter, manim.Text(
                            "k = " + str(k+1), color=manim.ORANGE
                        ).scale(0.75).move_to(self.k_counter))
                    )
                else:
                    self.play(
                        self.left_squares[i].animate.set_fill(
                            manim.BLUE, opacity=0.0),
                        self.array_squares[k].animate.set_fill(
                            manim.ORANGE, opacity=0.0),
                    )
                i = i + 1
            else:
                array[k] = right[j]
                inequality = manim.MathTex(r">", font_size=102)
                inequality.shift(manim.UP*0.30)
                self.play(manim.Create(inequality))
                self.replace_content(
                    self.right_contents[j], self.contents[k], k)
                self.play(manim.FadeOut(inequality))
                self.remove(inequality)
                # Increment j and iterator element
                if j+1 < len(self.right_squares) and k+1 < len(self.array_squares):
                    self.play(
                        self.right_squares[j+1].animate.set_fill(
                            manim.RED, opacity=0.5),
                        self.right_squares[j].animate.set_fill(
                            manim.RED, opacity=0.0),
                        self.array_squares[k].animate.set_fill(
                            manim.ORANGE, opacity=0.0),
                        self.array_squares[k+1].animate.set_fill(
                            manim.ORANGE, opacity=0.5),
                        manim.Transform(self.j_counter, manim.Text(
                            "j = " + str(j+1), color=manim.RED
                        ).scale(0.75).move_to(self.j_counter)),
                        manim.Transform(self.k_counter, manim.Text(
                            "k = " + str(k+1), color=manim.ORANGE
                        ).scale(0.75).move_to(self.k_counter))
                    )
                elif k+1 < len(self.array_squares) and i+1 <= len(self.left_squares):
                    self.play(
                        self.right_squares[j].animate.set_fill(
                            manim.RED, opacity=0.0),
                        self.array_squares[k].animate.set_fill(
                            manim.ORANGE, opacity=0.0),
                        self.array_squares[k+1].animate.set_fill(
                            manim.ORANGE, opacity=0.5),
                        manim.Transform(self.k_counter, manim.Text(
                            "k = " + str(k+1), color=manim.ORANGE
                        ).scale(0.75).move_to(self.k_counter))
                    )
                else:
                    self.play(
                        self.right_squares[j].animate.set_fill(
                            manim.RED, opacity=0.0),
                        self.array_squares[k].animate.set_fill(
                            manim.ORANGE, opacity=0.0),
                    )
                j = j + 1
            k = k + 1
        # Remaining elements from left
        while i < len(left):
            array[k] = left[i]
            self.replace_content(self.left_contents[i], self.contents[k], k)
            # Increment i and iterator element
            if i+1 < len(self.left_squares) and k+1 < len(self.array_squares):
                self.play(
                    self.left_squares[i+1].animate.set_fill(
                        manim.BLUE, opacity=0.5),
                    self.left_squares[i].animate.set_fill(
                        manim.BLUE, opacity=0.0),
                    self.array_squares[k].animate.set_fill(
                        manim.ORANGE, opacity=0.0),
                    self.array_squares[k+1].animate.set_fill(
                        manim.ORANGE, opacity=0.5),
                    manim.Transform(self.i_counter, manim.Text(
                        "i = " + str(i+1), color=manim.BLUE
                    ).scale(0.75).move_to(self.i_counter)),
                    manim.Transform(self.k_counter, manim.Text(
                        "k = " + str(k+1), color=manim.ORANGE
                    ).scale(0.75).move_to(self.k_counter))
                )
            elif k+1 < len(self.array_squares) and j+1 < len(self.right_squares):
                self.play(
                    self.left_squares[i].animate.set_fill(
                        manim.BLUE, opacity=0.0),
                    self.array_squares[k].animate.set_fill(
                        manim.ORANGE, opacity=0.0),
                    self.array_squares[k+1].animate.set_fill(
                        manim.ORANGE, opacity=0.5),
                    manim.Transform(self.k_counter, manim.Text(
                        "k = " + str(k+1), color=manim.ORANGE
                    ).scale(0.75).move_to(self.k_counter))
                )
            else:
                self.play(
                    self.left_squares[i].animate.set_fill(
                        manim.BLUE, opacity=0.0),
                    self.array_squares[k].animate.set_fill(
                        manim.ORANGE, opacity=0.0),
                )
            i = i + 1
            k = k + 1
        # Remaining elements from right
        while j < len(right):
            array[k] = right[j]
            self.replace_content(self.right_contents[j], self.contents[k], k)
            # Increment j and iterator element
            if j+1 < len(self.right_squares) and k+1 < len(self.array_squares):
                self.play(
                    self.right_squares[j+1].animate.set_fill(
                        manim.RED, opacity=0.5),
                    self.right_squares[j].animate.set_fill(
                        manim.RED, opacity=0.0),
                    self.array_squares[k].animate.set_fill(
                        manim.ORANGE, opacity=0.0),
                    self.array_squares[k+1].animate.set_fill(
                        manim.ORANGE, opacity=0.5),
                    manim.Transform(self.j_counter, manim.Text(
                        "j = " + str(j+1), color=manim.RED
                    ).scale(0.75).move_to(self.j_counter)),
                    manim.Transform(self.k_counter, manim.Text(
                        "k = " + str(k+1), color=manim.ORANGE
                    ).scale(0.75).move_to(self.k_counter))
                )
            else:
                self.play(
                    self.right_squares[j].animate.set_fill(
                        manim.RED, opacity=0.0),
                    self.array_squares[k].animate.set_fill(
                        manim.ORANGE, opacity=0.0),
                )
            j = j + 1
            k = k + 1

        # Fade
        self.play(
            self.array_squares[k - 1].animate.set_fill(
                manim.ORANGE, opacity=0.0),
            self.left_group.animate.fade_to("#000000", 1.0),
            self.right_group.animate.fade_to("#000000", 1.0),
        )
        self.remove(self.left_group, self.right_group)

    def merge_sort(self, array, first, last):
        """
        The main sorting alogrithm
        """
        if first >= last:
            return
        mid = (first+last)//2
        self.merge_sort(array, first, mid)
        self.merge_sort(array, mid+1, last)
        self.merge(array, first, mid, last)

    def construct(self):
        array = [5, 1, 7, 32, 8, 3, 8, 2, 4, 67]

        self.array_group, self.array_squares, self.contents = array_to_vgroup(
            array, "k")
        self.array_group.move_to(manim.ORIGIN)
        self.add(self.array_group)
        self.play(self.array_group.animate.shift(manim.UP*2))

        # Add counters
        self.k_counter = manim.Text(
            "k = 0", color=manim.ORANGE
        ).scale(0.75).to_edge(manim.UP)
        self.j_counter = manim.Text(
            "j = 0", color=manim.RED
        ).scale(0.75).next_to(self.k_counter, manim.RIGHT, buff=1.0)
        self.i_counter = manim.Text(
            "i = 0", color=manim.BLUE
        ).scale(0.75).next_to(self.k_counter, manim.LEFT, buff=1.0)
        self.play(
            manim.Create(self.i_counter),
            manim.Create(self.j_counter),
            manim.Create(self.k_counter),
        )

        # Start the algorithm
        self.merge_sort(array, 0, len(array)-1)
        self.play(
            self.array_group.animate.shift(manim.DOWN*2),
            manim.FadeOut(self.i_counter),
            manim.FadeOut(self.j_counter),
            manim.FadeOut(self.k_counter),
        )
        self.wait(2)
