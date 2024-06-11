class Car:
    price = 1000000

    def horse_powers(self):
        return "Количество лошадиных сил для автомобиля не указано"

class Nissan(Car):
    price = 1200000

    def horse_powers(self):
        return 200

class Kia(Car):
    price = 900000

    def horse_powers(self):
        return 150


nissan_car = Nissan()
kia_car = Kia()

print(f"Nissan: vehicle_type = 'car', price = {nissan_car.price}, horse_powers = {nissan_car.horse_powers()}")


print(f"Kia: vehicle_type = 'car', price = {kia_car.price}, horse_powers = {kia_car.horse_powers()}")
