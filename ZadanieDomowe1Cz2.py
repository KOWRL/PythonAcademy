#!/usr/bin/env python3

class Flower:
    def __init__(self, name, color, shape):
        self.name = name
        self.color = color
        self.shape = shape


name = input("Jak nazwê nosi kwiat: ")
color = input("Jakiego koloru jest kwiat: ")
shape = input("Jaki kszta³tu jest kwiat:  ")

print(name, color, shape);