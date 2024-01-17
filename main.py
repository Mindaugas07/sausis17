from typing import Generator, List
from random import randint

# def infinite_range(start: int = 0) -> Generator[int, None, None]:
#     current = start
#     while True:
#         yield current
#         current += 1


# # Usage
# counter = 0
# for value in infinite_range(10):
#     print(value)
#     counter += 1
#     if counter == 5:
#         break


# def squares_generator(n: int) -> Generator[int, None, None]:
#     for i in range(n):
#         yield i**2


# for value in squares_generator(5):
#     print(value)


# def random_num_generator(
#     n: int, low_interval_num: int, high_interval_num: int
# ) -> Generator[int, None, None]:
#     for _ in range(n):
#         yield randint(low_interval_num, high_interval_num)

# def random_numbers(how_many_numbers, *args):
#     low_interval_num = int(input("Please enter low number: "))
#     high_interval_num = int(
#         input(
#             "Please enter high number. It should be higher than low number and the difference must be higher than n: "
#         )
#     )
#     while high_interval_num - low_interval_num < how_many_numbers:
#         high_interval_num = int(
#             input(
#                 "Please enter high number. It should be higher than low number and the difference must be higher than n: "
#             )
#         )
#     for number in random_num_generator(
#         how_many_numbers, low_interval_num, high_interval_num
#     ):
#         print(number)

# random_numbers(8)


# def fibonacci(n: int) -> Generator[int, None, None]:
#     num1 = 0
#     num2 = 1
#     next_number = num2
#     count = 1
#     while count <= n:
#         yield next_number
#         count += 1
#         num1, num2 = num2, next_number
#         next_number = num1 + num2


# for number in fibonacci(8):
#     print(number)

# member_list = ["a", 2, "LJL", 4.5]


# def numbers_from_list(list_with_numbers_strings: list) -> Generator[int, None, None]:
#     for member in list_with_numbers_strings:
#         if type(member) == int or type(member) == float:
#             yield member


# for member in numbers_from_list(member_list):
#     print(member)


persons = [("Ona", 15, "Trakai", 4500.0), ("Vytautas", 45, "Kernave", 0.0)]


def filtering_gen(list_of_tuples: List[tuple], age: int) -> Generator[int, None, None]:
    for person_tuple in list_of_tuples:
        if person_tuple[1] < age:
            yield person_tuple


for person in filtering_gen(persons, 40):
    print(person)


def maping_gen(list_of_tuples: List[tuple]) -> Generator[int, None, None]:
    pass


def aggregation_gen(list_of_tuples: List[tuple]) -> Generator[int, None, None]:
    salary_sum = 0
    for index, person_tuple in enumerate(list_of_tuples):
        salary_sum += person_tuple[3]
    return salary_sum / (index + 1)


print(aggregation_gen(persons))
