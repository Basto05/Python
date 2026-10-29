
# ZADANIE 4.2

def make_ruler(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n musi być nieujemną liczbą całkowitą")

    return "|" + "....|" * n


def make_grid(rows, cols):
    if (not isinstance(rows, int) or isinstance(rows, bool)
            or not isinstance(cols, int) or isinstance(cols, bool)
            or rows < 0 or cols < 0):
        raise ValueError("Wymiary muszą być nieujemnymi liczbami całkowitymi")

    line = "+---" * cols + "+\n"
    inside = "|   " * cols + "|\n"

    return line + (inside + line) * rows


# TESTY 4.2

assert make_ruler(0) == "|"
assert make_ruler(1) == "|....|"
assert make_ruler(3) == "|....|....|....|"

assert make_grid(0, 0) == "+\n"
assert make_grid(1, 1) == "+---+\n|   |\n+---+\n"
assert make_grid(2, 2) == (
    "+---+---+\n"
    "|   |   |\n"
    "+---+---+\n"
    "|   |   |\n"
    "+---+---+\n"
)


# ZADANIE 4.3

def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n musi być nieujemną liczbą całkowitą")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


# TESTY 4.3

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(3) == 6
assert factorial(5) == 120
assert factorial(10) == 3628800


# ZADANIE 4.4

def fibonacci(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n musi być nieujemną liczbą całkowitą")

    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


# TESTY 4.4

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(5) == 5
assert fibonacci(10) == 55
assert fibonacci(15) == 610


# ZADANIE 4.5

# Wersja iteracyjna

def odwracanie(L, left, right):
    if not isinstance(left, int) or isinstance(left, bool):
        raise ValueError("Nieprawidłowy indeks")

    if not isinstance(right, int) or isinstance(right, bool):
        raise ValueError("Nieprawidłowy indeks")

    if left < 0 or right >= len(L) or left > right:
        raise ValueError("Nieprawidłowy zakres")

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


# Wersja rekurencyjna

def odwracanie_rekurencyjne(L, left, right):
    if not isinstance(left, int) or isinstance(left, bool):
        raise ValueError("Nieprawidłowy indeks")

    if not isinstance(right, int) or isinstance(right, bool):
        raise ValueError("Nieprawidłowy indeks")

    if left < 0 or right >= len(L) or left > right:
        raise ValueError("Nieprawidłowy zakres")

    if left >= right:
        return

    L[left], L[right] = L[right], L[left]

    odwracanie_rekurencyjne(L, left + 1, right - 1)


# TESTY 4.5

L = [1, 2, 3, 4, 5]
odwracanie(L, 1, 3)
assert L == [1, 4, 3, 2, 5]

L = [1, 2, 3, 4, 5]
odwracanie(L, 0, 4)
assert L == [5, 4, 3, 2, 1]

L = [1, 2, 3, 4, 5]
odwracanie_rekurencyjne(L, 1, 3)
assert L == [1, 4, 3, 2, 5]

L = [1, 2, 3, 4, 5]
odwracanie_rekurencyjne(L, 0, 4)
assert L == [5, 4, 3, 2, 1]


# ZADANIE 4.6

def sum_seq(sequence):
    result = 0

    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        elif isinstance(item, (int, float)) and not isinstance(item, bool):
            result += item
        else:
            raise ValueError("Sekwencja może zawierać tylko liczby")

    return result


# TESTY 4.6

assert sum_seq([]) == 0
assert sum_seq([1, 2, 3]) == 6
assert sum_seq([1, (2, 3), 4]) == 10
assert sum_seq([1, [2, [3, 4]], 5]) == 15
assert sum_seq((1, (2, 3), [4, 5])) == 15
assert sum_seq([1.5, [2.5, 3]]) == 7.0


# ZADANIE 4.7

def flatten(sequence):
    result = []

    for item in sequence:
        if isinstance(item, (list, tuple)):
            result.extend(flatten(item))
        else:
            result.append(item)

    return result


# TESTY 4.7

assert flatten([]) == []
assert flatten([1, 2, 3]) == [1, 2, 3]
assert flatten([1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert flatten([[1, 2], [[3, 4], 5]]) == [1, 2, 3, 4, 5]
assert flatten((1, (2, (3, 4)))) == [1, 2, 3, 4]
