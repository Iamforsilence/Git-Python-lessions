# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar,
# SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При
# значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


# У меня сомнения, что я правильно понял некоторые формулировки задачи.:)


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

        if self.is_police:
            self.is_police = "Полицейская"
        else:
            self.is_police = "Не полицейская"

    def go(self):
        if self.speed > 0:
            return "Машина едет"
        else:
            return "Машина стоит"

    def stop(self):
        if self.speed == 0:
            return "Машина стоит"
        else:
            return "Машина едет"

    def turn(self):
        return f"Поворот руля в в какую_то сторону"

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.length_car_limit = 4200
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Вы превысили скорость!"
        elif 0 < self.speed <= 60:
            return "Машина едет"
        else:
            return "Машина стоит"


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.limit_passengers = 4
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Вы превысили скорость!"
        elif 0 < self.speed <= 40:
            return "Машина едет"
        else:
            return "Машина стоит"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.price = 8980100
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.unit_weapon = "shotgun"
        super().__init__(speed, color, name, is_police)


car_1 = TownCar(70, "black", "Mazda", False)
print(f"Машина {car_1.name}, {car_1.color} цвета имеет скорость {car_1.speed}. Она {car_1.is_police}, и имеет длинну "
      f"{car_1.length_car_limit} м.")
print(car_1.go(), car_1.show_speed(), car_1.turn())

car_2 = WorkCar(50, "blue", "opel", False)
print(f"Машина {car_2.name}, {car_2.color} цвета имеет скорость {car_2.speed}. Она {car_2.is_police}, и имеет лимит "
      f"пассажиров,а именно {car_2.limit_passengers} человека.")
print(car_2.go(), car_2.show_speed(), car_2.turn())

car_3 = SportCar(120, "red", "dodge", False)
print(f"Машина {car_3.name}, {car_3.color} цвета имеет скорость {car_3.speed}. Она {car_3.is_police}, и ее цена "
      f"{car_3.price} рублей.")
print(f"{car_3.go()}, {car_3.turn()}, скорость равна {car_3.show_speed()}")

car_4 = PoliceCar(0, "white", "lada", True)
print(f"Машина {car_4.name}, {car_4.color} цвета имеет скорость {car_4.speed}. Она {car_4.is_police},и в ней лежит"
      f" {car_4.unit_weapon}.")
print(f"{car_4.stop()}, {car_4.turn()}, скорость равна {car_3.show_speed()}")
