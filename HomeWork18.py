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

print(f"Nissan цена: {nissan_car.price}")
print(f"Nissan лошадиные силы: {nissan_car.horse_powers()}")

print(f"Kia цена: {kia_car.price}")
print(f"Kia лошадиные силы: {kia_car.horse_powers()}")
