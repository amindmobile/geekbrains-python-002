# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


# Можно решить с помощью FOR-WHILE, но Ребе скажет, что это не кошерно, т.к. откровение гласит:
# "Для решения используйте цикл while и арифметические операции."
# user_Number = input("Введите целое положительное число состоящее не менее чем из двух цифр: ")
# most_Bigger_number = 0
# for i in user_Number:
#     while int(i) > most_Bigger_number:
#         most_Bigger_number = int(i)
# print(most_Bigger_number)


# Поэтому решаем кошернее, но Ребе снова будет недоволен:
# user_Number = input("Введите целое положительное число состоящее не менее чем из двух цифр: ")
# print(f'В введённом вами числе {user_Number} максимальная цифра таки: {max(user_Number)}')


# финальный вариант, но всё равно с опаской косимся на Ребе, потому что про if он не говорил
user_Number = int(input("Введите целое положительное число состоящее не менее чем из двух цифр: "))
max_Cyfer = 0
while user_Number > 1:
    residue = user_Number % 10
    user_Number = user_Number // 10
    max_Cyfer = residue if residue > max_Cyfer else max_Cyfer
print(f"Максимальная цифра: {max_Cyfer}")
