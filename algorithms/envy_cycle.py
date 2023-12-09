class Node:
    def __init__(self):
        self.color = "WHITE"
        self.parent = None
        self.discovery = None
        self.finish = None


def detect_envy_cycle(n, values):
    nodes = [Node() for _ in range(n)]
