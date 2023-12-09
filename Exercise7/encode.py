#!/usr/bin/python3
# coding=utf-8


def encode(data, encoding):
    encoded = ""
    for character in data:
        encoded += encoding[character]
    return encoded
