# !/usr/bin/python3
# coding=utf-8

class Queue:
    def __init__(self, max_size):
        self.queue = [None]*max_size
        self.head = 0
        self.tail = 0
        self.size = max_size

    def enqueue(self, value):
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.size

    def dequeue(self):
        value = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        return value
