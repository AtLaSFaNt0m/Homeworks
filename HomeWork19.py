class Vehicle:
    __COLOR_VARIANTS = ['Red', 'Blue', 'Green', 'Black', 'White']

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

    def get_passengers_limit(self):
        return self.__PASSENGERS_LIMIT


# Пример использования
vehicle = Vehicle("Alice", "Toyota", 150, "Red")
vehicle.print_info()
vehicle.set_color("Blue")
vehicle.print_info()
vehicle.set_color("Yellow")

sedan = Sedan("Bob", "Honda", 180, "Black")
sedan.print_info()
print(f"Лимит пассажиров: {sedan.get_passengers_limit()}")
