# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.

filename = 'lesson_05_01.txt'
exit_from_program = False

while not exit_from_program:
    request = input(f'Введите что-нибудь и я запишу это в файл {filename}: ')
    with open(filename, "a") as file:
        if request:
            file.writelines(request + '\n')
        else:
            exit_from_program = True
            print("Вы ничего не ввели, запись в файл остановлена.")
            break
