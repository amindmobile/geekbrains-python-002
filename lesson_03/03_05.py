#  Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
#  чисел.
#
#  Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
#  чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
#  программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
#  чисел к полученной ранее сумме и после этого завершить программу.


def nervous_shitty_func():
    global_result = 0
    exit_from_program = False
    while not exit_from_program:
        user_numbers = input('Введите несколько цифр через пробел, или Q для выхода: ').split()
        temp_result = 0
        for user_number in range(len(user_numbers)):
            if user_numbers[user_number].upper() == 'Q':
                exit_from_program = True
                break
            else:
                temp_result = temp_result + int(user_numbers[user_number])
        global_result = global_result + temp_result
        print(f'Промежуточная сумма: {global_result}')
    print(f'Финальная сумма: {global_result}')


nervous_shitty_func()
