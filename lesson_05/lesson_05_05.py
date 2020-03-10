# 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce
super_database_file = 'lesson_05_05.txt'

print(*range(3, 624), file=open(super_database_file, 'w'))

with open(super_database_file, 'r') as file:
    for line in file:
        print(sum(map(int, line.strip().split(' '))))
