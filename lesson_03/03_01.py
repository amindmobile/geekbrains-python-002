#  Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#  Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def your_division():
    try:
        first_value = int(input("Введите делимое число: "))
        second_value = int(input("Введите число-делитель: "))
        return f"Результат деления: {first_value / second_value}"
    except ZeroDivisionError:
        return "На ноль делить нельзя"


print(your_division())
