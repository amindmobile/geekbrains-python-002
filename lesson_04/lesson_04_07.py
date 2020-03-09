# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
# за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial
from functools import reduce
from itertools import count


def fact():
    for item in count(1):
        yield factorial(item)


gena = fact()
counter = 0
for i in gena:
    if counter == 10:
        break
    else:
        counter += 1
        print(f"Factorial {counter} = {i}")


#
# def fact(iterable):
#     for element in iterable:
#         yield factorial(element)
#
#
# for i in fact([1, 2, 3, 4, 5]):
#     print(i)
#
#
# numbers = [1, 2, 3, 4, 5]
#
#
# # додумаю позже
#
# limit = 5
# print(
#   reduce(
#     (lambda i, j: i*j),
#     range(1, limit+1)
#   )
# )

#
#
# def fac(n):
#     for i in n:
#         return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
#
#
# num = [1, 2, 3, 4, 5]
# print("Factorial of", num, "is", fac(num))


# for i in numbers in range(2, numbers + 1):
#     factorial *= i
#
# print(factorial)
