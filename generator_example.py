def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci2(n):
    a, b = 0, 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i = i + 1


def factorial(n):
    def factorial_generator():
        a = 1
        i = 1
        while True:
            yield a
            i = i + 1
            a = a * i
    factorial_generator = factorial_generator()
    for i in range(n):
        result = next(factorial_generator)
    return result


if __name__ == "__main__":
    # fibos = fibonacci()
    # print(next(fibos))
    # print(next(fibos))
    #
    # fibos2 = fibonacci2(5)
    # for num in fibos2:
    #     print(num)

    print(factorial(5))
