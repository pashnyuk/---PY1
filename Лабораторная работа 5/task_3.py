from random import random


def get_unique_list_numbers(start, stop, step) -> list[int]:
    list_numbers = []
    i = 0
    value = start
    while value < stop:
        list_numbers.append(value)
        i += 1
        value = start + i
    return list_numbers


list_unique_numbers = get_unique_list_numbers(-10, 11, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
