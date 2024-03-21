from typing import Callable
import re


def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    total_income = sum(func(text))
    return total_income


text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний 
        дохід, доповнений додатковими надходженнями 27.45 i 324.00 доларів."""


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
