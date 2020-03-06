# 1)	Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.
from sys import argv


def salary_calc():  # Рассчитать зарплату
    return f'{(work_hours * rate_per_hour) + bonus}'


def help_me():  # Получить помощь
    help_list = ['Запуск без параметров - покажу этот текст помощи',
                 'Запуск с параметрами через пробел(только цифры): '
                 '"Выработка в часах", "Ставка в час", "Премия" - вычислю зарплату.', ]
    for help_text in help_list:
        print(help_text)


try:
    work_hours = int(argv[1])
    rate_per_hour = int(argv[2])
    bonus = int(argv[3])
    print(f'Выработка в часах: {work_hours}')
    print(f'Ставка в час: {rate_per_hour}')
    print(f'Премия:  {bonus}')
    print(f'Заработная плата: {salary_calc()}')
except ValueError as error_message_ve:
    print(error_message_ve)
    help_me()
except IndexError as error_message_ie:
    print(error_message_ie)
    help_me()
