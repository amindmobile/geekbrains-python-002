# task 6.1
#  Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
#  первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(word):
    return str(word.capitalize())


print(int_func('слово'))


# task 6.2
#  Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
#  состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
#  заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
def int_func():
    one_line_list = []
    words = ['forest', 'lama', 'kutrapali', 'mango', 'lazarus', 'piston']
    # words = input('Введите несколько ЛАТИНСКИХ (хз почему) слов через пробел: ').split()
    for word in words:
        one_line_list.append(str(word.capitalize()))  # можно было остановиться здесь, но надо выводить одной строкой
    print(" ".join(one_line_list))


int_func()
