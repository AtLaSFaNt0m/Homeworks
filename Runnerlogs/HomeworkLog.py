import unittest
import logging
from Homework48 import Runner  # Предположим, что класс Runner находится в файле runner.py

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(levelname)s: %(message)s"
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            # Попытка создать объект Runner с отрицательной скоростью
            runner = Runner(name="Test Runner", speed=-5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)  # Это не должно быть выполнено
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            # Попытка создать объект Runner с неверным типом для имени
            runner = Runner(name=123, speed=5)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)  # Это не должно быть выполнено
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)

if __name__ == "__main__":
    unittest.main()
