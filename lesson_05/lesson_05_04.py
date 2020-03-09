# 4)	Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


def file_read(file_to_read):
    with open(file_to_read, 'r') as the_file:
        return the_file.read()


file_source = 'lesson_05_04.txt'
file_out = 'lesson_05_04_out.txt'
out_list = []
en_rus_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open(file_source, 'r') as file:
    for line in file:
        line = line.split(' ', 1)
        out_list.append(f'{en_rus_dict[line[0]]} {line[1]}')
with open(file_out, 'w') as file:
    file.writelines(out_list)
print(f'\nБыло :\n{file_read(file_source)}\n\nСтало :\n{file_read(file_out)}')
