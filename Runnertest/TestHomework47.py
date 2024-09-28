import unittest
from Homework47 import RunnerTest, TournamentTest


# Создание TestSuite
def suite():
    suite = unittest.TestSuite()

    # Загрузка тестов из классов RunnerTest и TournamentTest
    loader = unittest.defaultTestLoader
    suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

    return suite


if __name__ == '__main__':
    # Запуск тестов
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
