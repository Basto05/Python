# ZADANIE 7.6

import random


def iterator01():
    while True:
        yield 0
        yield 1


def random_direction():
    directions = ("N", "E", "S", "W")

    while True:
        yield random.choice(directions)


def iterator_weekdays():
    day = 0

    while True:
        yield day
        day = (day + 1) % 7
