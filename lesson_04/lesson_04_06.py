# Реализовать два небольших скрипта:  
# а) итератор, генерирующий целые числа, начиная с указанного,  
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не
# должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором
# также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle

# a)
print("exercise a): (Number generator from 3 to 10")
for i in count(3):
    if int(i) >= 11:
        break
    else:
        print(i)

# b)
print("Exercise b) (Cycling print the list contents for 10 times: ")
random_list = ['ночью, ёжик, марципан, вилкой, радует, банан']
counter = 0
for i in cycle(random_list):
    if counter >= 10:
        break
    else:
        print(i)
        counter += 1

random_list_1 = ["если", "ловкий", "огурец", "танк", "летит", "быстрей", "коня"]


def cycl_1(iterable):
    counting = 0
    for item in cycle(iterable):
        if counting >= len(iterable):
            break
        else:
            yield item
            counting += 1

print("Yielding the list by its length:  ")
print(*cycl_1(random_list_1))
