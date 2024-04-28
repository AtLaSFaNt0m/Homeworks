def test(*args):
    for arg in args:
        print(arg)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


test(1, "Hello", 3.14, [1, 2, 3])
result = factorial(5)
print("Factorial of 5 is:", result)
