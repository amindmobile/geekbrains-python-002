# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

# variant_0
print([number for number in range(20, 240) if number % 20 == 0 or number % 21 == 0])

# variant_1 (better)
print([number for number in range(20, 240) if not all((number % 20, number % 21))])
