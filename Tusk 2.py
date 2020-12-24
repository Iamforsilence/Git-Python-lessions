# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.mass_asphalt_on_1cm = 100
        self.depth_asphalt = 5

    def mass_asphalt(self):
        mass = self._length * self._width * self.mass_asphalt_on_1cm * self.depth_asphalt
        print(mass)


quantity_asphalt = Road(10, 2)
quantity_asphalt.mass_asphalt()
