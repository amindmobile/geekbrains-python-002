# 6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий
# по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                         Физика:   30(л)   —   10(лаб)
#                                         Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

lessons = {}
numbers = [str(n) for n in range(10)]
with open('lesson_05_06.txt', 'r') as file_with_data:
    for line in file_with_data:
        subject, *raw = line.split()
        subject = subject.replace(':', '')
        lessons[subject] = 0
        for hours in raw:
            hours = "".join(char for char in hours if char in numbers)
            lessons[subject] += int(hours) if hours else 0

print(lessons)

# ниже следуют нездоровые варианты мутаций

from itertools import groupby
from functools import reduce


# def list_sum(num_list):
#     the_sum = 0
#     for i in num_list:
#         the_sum = the_sum + i
#     return the_sum


# out = {}
# with open('lesson_05_06.txt', 'r') as f:
#     for line in f:
#         raw = line.split()
#         subject = raw[0][:-1]
#         hours = [x.split('(')[0] for x in raw[1:] if x != '—']
#         out[subject] = sum(map(int, hours))


# можно и таким красивым вариантом, но некогда было доделать
# ---------------------------------------------------------------------------
# def get_digit(info):
#     digit = [int(''.join(i)) for is_digit, i in groupby(info, str.isdigit) if is_digit]
#     for number in digit:
#         return number
#
# # ---------------------------------------------------------------------------
# study_database = {}
# temp_list = []
# with open('lesson_05_06.txt', 'r') as super_database_file:
#     for line in super_database_file:
#         subject, lecture, practice, lab = line.split()
#         lecture_digit = get_digit(lecture)
#         practice_digit = get_digit(practice)
#         lab_digit = get_digit(lab)
#
#         print(f'{subject} {get_digit(lecture)}+{get_digit(practice)}')
        # print(get_digit(lecture) + get_digit(practice))
# ---------------------------------------------------------------------------

#  Вполне рабочий вариант, не додумал, додумаю
# with open('lesson_05_06.txt', 'r') as super_database_file:
#     for line in super_database_file:
#         l_name, l_info = line.split(':')
#         l_info = (item for item in l_info.strip().split(' ') if item)
#         l_info = {l_name: [i if i != '=' else None for i in l_info]}
#         print(l_info)


        # print(list_sum(get_digit(lecture)))

    #     print(subject, lecture, practice, lab)
    #     study_database[subject] = int(lecture) + int(practice) + int(lab)
    # print(f'Общее количество часов по предмету - \n {study_database}')


# mydict[subj] += int(i[:i.find("(")])


# print(sum(map(int, line.strip().split(' '))))
