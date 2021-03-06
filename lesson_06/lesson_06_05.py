# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Включаем рисовашку')


class Pen(Stationery):
    def draw(self):
        print('Ручка пишет')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш рисует')


class Marker(Stationery):
    def draw(self):
        print('Маркер мажет')


pen = Pen('ручка')
pencil = Pencil('карандаш')
marker = Marker('маркер')

pen.draw()
pencil.draw()
marker.draw()
