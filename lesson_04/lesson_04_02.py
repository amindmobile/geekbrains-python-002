# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
import random

# variant_0
lst0 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_0 = [lst0[i + 1] for i in range(0, len(lst0) - 1) if lst0[i + 1] > lst0[i]]
print("Вариант 0:")
print(lst0)
print(result_0)

# variant_1
lst1 = [random.randint(10, 50) for number in range(50)]
result_1 = [lst1[i + 1] for i in range(0, len(lst1) - 1) if lst1[i + 1] > lst1[i]]
print("Вариант 1:")
print(lst1)
print(result_1)

# variant_2
lst2 = [random.randint(10, 50) for number in range(random.randrange(10, 90), random.randrange(100, 200))]
result_2 = [lst2[i + 1] for i in range(0, len(lst2) - 1) if lst2[i + 1] > lst2[i]]
print("Вариант 2:")
print(lst2)
print(result_2)

# variant_3 (результат теперь содержит уникальные значения)
lst3 = [random.randint(10, 50) for number in range(random.randrange(10, 90), random.randrange(100, 200))]
result_3 = sorted(set([lst3[i + 1] for i in range(0, len(lst3) - 1) if lst3[i + 1] > lst3[i]]))
print("Вариант 3:")
print(lst3)
print(result_3)
