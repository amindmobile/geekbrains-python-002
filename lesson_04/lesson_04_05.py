# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

# в python 3.x reduce() устарело!
# hint: sum = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
from functools import reduce

# variant_0
print(reduce(lambda first, second: first + second, [num for num in range(100, 1001) if not num % 2]))

# variant_1 (better)
print(reduce(lambda first, second: first + second, [num for num in range(100, 1001, 2)]))
