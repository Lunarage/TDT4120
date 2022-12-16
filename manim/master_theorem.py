import manim
from manim import Scene, UP, DOWN, LEFT, RIGHT, VGroup


class MasterTheorem(Scene):
    def construct(self):

        self.camera.background_color = "#333333"

        tree = VGroup()

        root = manim.MathTex(r"cf(n)")
        root.to_edge(UP)
        self.add(root)
        tree += root

        leaves_1 = [manim.MathTex(r"cf(n/b)"), manim.MathTex(r"cf(n/b)")]
        leaves_1_vg = VGroup(*leaves_1).arrange(buff=3.5)
        leaves_1_vg.next_to(root, DOWN, buff=1.5)
        self.add(leaves_1_vg)
        tree += leaves_1_vg

        lines_1 = [
            manim.Line().put_start_and_end_on(
                root.get_bottom(), leaves_1[0].get_top()),
            manim.Line().put_start_and_end_on(
                root.get_bottom(), leaves_1[1].get_top()),
        ]
        lines_1_vg = VGroup(*lines_1)
        self.add(lines_1_vg)
        tree += lines_1_vg

        leaves_2 = [
            manim.MathTex(r"cf(n/b^2)"),
            manim.MathTex(r"cf(n/b^2)"),
            manim.MathTex(r"cf(n/b^2)"),
            manim.MathTex(r"cf(n/b^2)"),
        ]
        leaves_2_vg = VGroup(*leaves_2).arrange(buff=1.0)
        leaves_2_vg.next_to(leaves_1_vg, DOWN, buff=1.5)
        self.add(leaves_2_vg)
        tree += leaves_2_vg

        lines_2 = [
            manim.Line().put_start_and_end_on(
                leaves_1[0].get_bottom(), leaves_2[0].get_top()),
            manim.Line().put_start_and_end_on(
                leaves_1[0].get_bottom(), leaves_2[1].get_top()),
            manim.Line().put_start_and_end_on(
                leaves_1[1].get_bottom(), leaves_2[2].get_top()),
            manim.Line().put_start_and_end_on(
                leaves_1[1].get_bottom(), leaves_2[3].get_top()),
        ]
        lines_2_vg = VGroup(*lines_2)
        self.add(lines_2_vg)
        tree += lines_2_vg

        bottom_dots = [
            manim.MathTex(r"\vdots"),
            manim.MathTex(r"\vdots"),
            manim.MathTex(r"\vdots"),
            manim.MathTex(r"\vdots"),
        ]
        bottom_dots_vg = VGroup(*[dots.next_to(leaves_2[index], DOWN, buff=0.25)
                                for index, dots in enumerate(bottom_dots)])
        self.add(bottom_dots_vg)
        tree += bottom_dots_vg

        leaves_bottom = [
            manim.MathTex(r"\Theta(1)"),
            manim.MathTex(r"\Theta(1)"),
            manim.MathTex(r"\Theta(1)"),
            manim.MathTex(r"\Theta(1)"),
        ]
        leaves_bottom_vg = VGroup(*[leaf.next_to(bottom_dots[index], DOWN, buff=0.25)
                                    for index, leaf in enumerate(leaves_bottom)])
        self.add(leaves_bottom_vg)
        tree += leaves_bottom_vg

        height_line = manim.DoubleArrow(
            tree.get_corner(UP + LEFT) + UP*0.25,
            tree.get_corner(DOWN + LEFT) + DOWN*0.25,
        )
        height_line.to_edge(LEFT, buff=1.5)
        self.add(height_line)
        height_label = manim.MathTex(r"\log_b n").move_to(height_line).add_background_rectangle(color="#333333", opacity=1.0)
        self.add(height_label)

        width_line = manim.DoubleArrow(
            tree.get_corner(DOWN + LEFT) + LEFT*0.5,
            tree.get_corner(DOWN + RIGHT) + RIGHT*0.5,
        )
        width_line.to_edge(DOWN, buff=0.75)
        self.add(width_line)
        width_label = manim.MathTex(r"a^{\log_b n} = n^{\log_b a}").move_to(width_line).add_background_rectangle(color="#333333", opacity=1.0)
        self.add(width_label)
