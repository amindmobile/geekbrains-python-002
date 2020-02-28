# на курсе этому не учили, но мы-то знаааем.. ;)
from itertools import zip_longest

#  Мутно, но иначе чистый инпут принимает просто строку и она потом итерируется посимвольно
user_list = list(map(int, input('Введите числа через пробел: ').split()))

nl = []
for a, b in zip_longest(user_list[::2], user_list[1::2]):
    if b:
        nl.append(b)
    if a:
        nl.append(a)
print(nl)
