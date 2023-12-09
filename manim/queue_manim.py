import random
from queue import Queue
from manim import Scene, Text, Table

class EnqueueNumbers(Scene):
    def construct(self):
        t0 = Table([
            [str(index) for index in range(3)],
            [str(random.randint(1, 10)) for index in range(3)]
            ])
        self.add(t0)
