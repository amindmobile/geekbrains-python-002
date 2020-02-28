# 4)	Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# 	Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

userWord = input().split()

for num, element in enumerate(userWord):
	if len(element) > 10:
		print(num, element[:10])
	else:
		print(num, element)
