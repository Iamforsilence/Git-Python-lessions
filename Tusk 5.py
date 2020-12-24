# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
# из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        return f"Вы используете {self.title}."


class Pencil(Stationery):
    def draw(self):
        return f"Вы используете {self.title}."


class Handle(Stationery):
    def draw(self):
        return f"Вы используете {self.title}."


blue_pen = Pen("Синяя ручка")
print(blue_pen.draw())
simple_pencil = Pencil("Простой карандаш")
print(simple_pencil.draw())
red_handle = Handle("Красный маркер")
print(red_handle.draw())
