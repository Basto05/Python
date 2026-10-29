# ZADANIE 5.2

from math import gcd


def simplify_frac(frac):
    if (not isinstance(frac, (list, tuple)) or len(frac) != 2
            or any(not isinstance(x, int) or isinstance(x, bool) for x in frac)):
        raise ValueError("Ułamek musi zawierać dwie liczby całkowite")

    a, b = frac

    if b == 0:
        raise ValueError("Mianownik nie może być zerem")

    divisor = gcd(a, b)

    a //= divisor
    b //= divisor

    if b < 0:
        a = -a
        b = -b

    return [a, b]


def add_frac(frac1, frac2):
    a, b = simplify_frac(frac1)
    c, d = simplify_frac(frac2)

    return simplify_frac([a * d + c * b, b * d])


def sub_frac(frac1, frac2):
    a, b = simplify_frac(frac1)
    c, d = simplify_frac(frac2)

    return simplify_frac([a * d - c * b, b * d])


def mul_frac(frac1, frac2):
    a, b = simplify_frac(frac1)
    c, d = simplify_frac(frac2)

    return simplify_frac([a * c, b * d])


def div_frac(frac1, frac2):
    a, b = simplify_frac(frac1)
    c, d = simplify_frac(frac2)

    if c == 0:
        raise ValueError("Nie można dzielić przez zero")

    return simplify_frac([a * d, b * c])


def is_positive(frac):
    a, b = simplify_frac(frac)

    return a > 0


def is_zero(frac):
    a, b = simplify_frac(frac)

    return a == 0


def cmp_frac(frac1, frac2):
    a, b = simplify_frac(frac1)
    c, d = simplify_frac(frac2)

    difference = a * d - c * b

    if difference < 0:
        return -1
    elif difference > 0:
        return 1
    else:
        return 0


def frac2float(frac):
    a, b = simplify_frac(frac)

    return a / b