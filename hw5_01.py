# Module 5 Homework: Exercise 1
# This function generates Fibonacci numbers using cache to store and return numbers that have already been generated.


def caching_fibonacci(n):
    cache = {}

    def fibonacci(n) -> int:
        if n <= 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            if n in cache:
                result = cache[n]
            else:
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
                result = cache[n]
        return result
    return fibonacci(n)


# Get Fibonacci function (assign fibonacci function to fib)
fib = caching_fibonacci()

# Use
print(fib(10))  # Returns 55
print(fib(15))  # Returns 610
print(fib(-5))  # Returns 0
print(fib(0))  # Returns 0
print(fib(1))  # Returns 1
