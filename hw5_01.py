# Module 5 Homework: Exercise 1
# This function generates Fibonacci numbers using cache to store and return numbers that have already been generated.


def caching_fibonacci():
    cache = {}

    def fibonacci(n) -> int:  # inner function which calculates the fibonacci number
        if n <= 0:  # return if n = 0
            result = 0
        elif n == 1:  # return 1 if n = 1
            result = 1
        else:
            if n in cache:  # if exists in cache return Fibonacci number from cache
                result = cache.get(n)
            else:  # calculate Fibonacci number and write to cache
                result = fibonacci(n - 1) + fibonacci(n - 2)
                cache[n] = result
        return result
    return fibonacci


# Get Fibonacci function (assign fibonacci function to fib, i.e. create a function fib)
fib = caching_fibonacci()

# Use fib function to calculate a Fibonacci number
print(fib(5))  # Returns 5
print(fib(10))  # Returns 55
print(fib(15))  # Returns 610
print(fib(-5))  # Returns 0
print(fib(0))  # Returns 0
print(fib(1))  # Returns 1
