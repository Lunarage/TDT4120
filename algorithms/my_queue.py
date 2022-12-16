# !/usr/bin/python3
# coding=utf-8


class Queue:
    def __init__(self, max_size):
        self.queue = []
        pass

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)
