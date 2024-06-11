class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car:
    def __init__(self):
        self.price = 1000000

    def horse_powers(self):
        return "Количество лошадиных сил для автомобиля не указано"

class Nissan(Car, Vehicle):
    def __init__(self):
        Car.__init__(self)
        Vehicle.__init__(self)
        self.price = 1200000
        self.vehicle_type = "car"

    def horse_powers(self):
        return 200


nissan_car = Nissan()


print(nissan_car.vehicle_type)
print(nissan_car.price)
