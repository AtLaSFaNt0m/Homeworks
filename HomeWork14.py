class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def horse_powers(self):
        return "Количество лошадиных сил для автомобиля не указано"

class Nissan(Car, Vehicle):
    price = 1200000
    vehicle_type = "car"

    def horse_powers(self):
        return 200


nissan_car = Nissan()

print(nissan_car.vehicle_type)
print(nissan_car.price)
