#  Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
#  аргументов.

#  Это решение в точности по ТЗ (но файлом выше решение мне больше нравится)


# variant 00
def bigger_sum00(num1, num2, num3):
    numbers_list = [num1, num2, num3]
    return sum(numbers_list) - min(numbers_list)


print(bigger_sum00(100, 11, 345))


# variant 01
def bigger_sum_01(*args):
    return sum(args) - min(args)


print(bigger_sum_01(100, 11, 345))


# variant 02
def bigger_sum02(num1, num2, num3):
    numbers_list = sorted([num1, num2, num3])
    return sum((numbers_list[1], numbers_list[2]))


print(bigger_sum02(100, 11, 345))


# variant 03
def bigger_sum03(a, b, c):
    numbers_list = [a, b, c]
    result_list = []
    number_max_1 = max(numbers_list)
    result_list.append(number_max_1)
    numbers_list.remove(number_max_1)
    number_max_2 = max(numbers_list)
    result_list.append(number_max_2)
    return sum(result_list)


print(bigger_sum03(100, 11, 345))


# variant 04
def bigger_sum04(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    result_list = numbers[-2:]
    return sum(result_list)


print(bigger_sum04(100, 11, 345))


# variant 05
def func(a, b, c):
    numbers = [a, b, c]
    return sum([a for a in numbers if a != min(numbers)])


print(func(100, 11, 345))
