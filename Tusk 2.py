# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Cloth:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def quantity_coat(self):
        return self.size / 6.5 + 0.5

    def quantity_suit(self):
        return self.height * 2 + 0.3

    @property
    def quantity_full(self):
        return str(f'Общий расход ткани \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Cloth):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.quantity_c = self.size / 6.5 + 0.5

    def __str__(self):
        return f'Расход ткани на пальто {self.quantity_c}'


class Suit(Cloth):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.quantity_s = self.height * 2 + 0.3

    def __str__(self):
        return f'Расход ткани на костюм {self.quantity_s}'


coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(coat.quantity_full)
print(suit.quantity_full)
print(coat.quantity_c)
print(suit.quantity_s)
