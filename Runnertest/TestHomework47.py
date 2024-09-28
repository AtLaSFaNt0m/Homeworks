import unittest
from Homework47 import RunnerTest, TournamentTest


def suite():
    suite = unittest.TestSuite()

    loader = unittest.defaultTestLoader
    suite.addTests(loader.loadTestsFromTestCase(RunnerTest))
    suite.addTests(loader.loadTestsFromTestCase(TournamentTest))

    return suite


if __name__ == '__main__':

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
