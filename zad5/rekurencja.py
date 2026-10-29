def factorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n musi być nieujemną liczbą całkowitą")

    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def fibonacci(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n musi być nieujemną liczbą całkowitą")

    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a