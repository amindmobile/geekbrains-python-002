# 1)	Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

list_ = [1, 7.40, ['list in list'], "строка", True, ("tuple1", "tuple2"), {'key': "value"}, bytes([55, 47, 32, 69])]
for i in list_:
	print(f"Элемент списка '{i}' обладает типом: {type(i)}")