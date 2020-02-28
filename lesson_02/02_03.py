# 3)Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

monthList = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь',
             'декабрь']
monthDict = {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь',
             7: 'июль', 8: 'август', 9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'}

userQuestion = int(input('Введите месяц в виде целого числа от 1 до 12: '))
season = None

if userQuestion in range(1, 2) or userQuestion == 12:
    season = 'зимний'
elif userQuestion in range(3, 5):
    season = 'весенний'
elif userQuestion in range(6, 8):
    season = 'летний'
elif userQuestion in range(9, 11):
    season = 'осенний'
else:
    print('Надо было ввести месяц в виде целого числа от 1 до 12')

print(f'(list reaction) В году {userQuestion}й месяц {season}, это {monthList[userQuestion - 1]}.')
print(f'(dict reaction) В году {userQuestion}й месяц {season}, это {monthDict.get(userQuestion)}.')
