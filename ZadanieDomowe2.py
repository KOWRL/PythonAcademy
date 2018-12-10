#!/usr/bin/env python3
class Flower:
    pass


class Potted(Flower):
    pass


class Orchid(Potted):
    pass


flower = Flower()
potted = Potted()
orchid = Orchid()

print(isinstance(orchid, Orchid))
print(isinstance(orchid, Potted))
print(isinstance(orchid, Flower))
print(isinstance(orchid, object))
