# 7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

profit_1 = {}
profit_2 = {}
profit_global = 0
prof_average = 0
counter = 0
database_file = 'lesson_05_07.txt'
json_file = 'lesson_05_07.json'

with open(database_file, 'r') as file:
    for line in file:
        name, firm, earnings, losses = line.split()
        profit_1[name] = int(earnings) - int(losses)
        if profit_1.setdefault(name) >= 0:
            profit_global = profit_global + profit_1.setdefault(name)
            counter += 1
    if counter != 0:
        prof_average = profit_global / counter
        print(f'Средняя прибыль: {prof_average:.2f}')
    else:
        print(f'Прибыли нет, но есть убыток.')
    profit_2 = {'средняя прибыль': round(prof_average)}
    profit_1.update(profit_2)
    print(f'Прибыль каждой компании: {profit_1}')

with open(json_file, 'w', encoding='utf8') as json_file_write:
    json.dump(profit_1, json_file_write, ensure_ascii=False)

    json_file_read = json.dumps(profit_1, ensure_ascii=False)
    print(f'Проверим верность записанной в json информации: \n '
          f' {json_file_read}')



