# Module 5 Homework: Exercise 2

import re
from typing import Callable
from decimal import Decimal


# This function identifies real numbers in the text and returns them as a generator.
def generator_numbers(text: str):
    pattern = r"\s[-]?\d*\.\d+\s"  # pattern for positive and negative decimal numbers with spaces on each side
    numbers = re.findall(pattern, text)

    for num in numbers:
        yield num


# Function sum_profit sums up the numbers from generator_numbers
def sum_profit(text: str, func: Callable):
    gen = func(text)
    total = 0
    for num in gen:
        total += Decimal(str(num))  # Uses Decimal for precision
    return total


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими "
        "надходженнями 27.45 і 324.00 доларів.")

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
