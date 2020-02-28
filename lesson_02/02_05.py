# 5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
# значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

ratingList = sorted([3, 7, 5, 9, 6, 2, 4])
new_rating = int(input('Введите цифру рейтинга от 0 до 9: '))

if new_rating in range(1, 9) and new_rating not in ratingList:
	ratingList.append(new_rating)
elif new_rating in ratingList:
	ratingList.insert(ratingList.index(new_rating), new_rating)
else:
	print('Some shit happen, we need a set of cool exceptions here')
ratingList.reverse()
ratingList.sort()
print(f'Новый лист рейтинга с учетом ваших изменений ({new_rating}): {ratingList}')
