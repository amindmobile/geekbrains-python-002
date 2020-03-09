# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32


file_to_work = 'lesson_05_03.txt'
with open(file_to_work, 'r') as file:
    salary_global, salary_small = [], []
    employees_list = file.read().split('\n')
    for line in employees_list:
        line = line.split()
        if float(line[1]) < 20000:
            salary_small.append(line[0])
        salary_global.append(line[1])
print(f'Оклад меньше 20 тыс. рублей у: {", ".join(map(str, salary_small))}.\n'
      f'Средний оклад по больнице: {round(sum(map(float, salary_global)) / len(salary_global))}')
