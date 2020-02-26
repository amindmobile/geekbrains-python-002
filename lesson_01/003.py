# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number_From_User = input("Enter number_From_User: ")
a = int(number_From_User * 2)
b = int(number_From_User * 3)
c = int(number_From_User + number_From_User)
d = int(number_From_User + number_From_User + number_From_User)


print(f'Вариант ab красивее и читабельнее: {int(number_From_User) + a + b}')
print(f'Вариант cd выполнен в соответствии с заданием: {(int(number_From_User) + c + d)}')
