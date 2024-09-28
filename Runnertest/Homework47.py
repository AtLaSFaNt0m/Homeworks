import unittest

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")
        else:
            return method(self, *args, **kwargs)
    return wrapper

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrew = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_walk(self):
        self.usain.walk()
        self.assertEqual(self.usain.distance, 10)

    @skip_if_frozen
    def test_run(self):
        self.usain.run()
        self.assertEqual(self.usain.distance, 20)

    @skip_if_frozen
    def test_challenge(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.__class__.all_results["usain_nick"] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(str(result[max(result.keys())]) == "Ник")


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", 10)
        self.andrew = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        self.__class__.all_results["usain_nick"] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(str(result[max(result.keys())]) == "Ник")

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.andrew, self.nick)
        result = tournament.start()
        self.__class__.all_results["andrew_nick"] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(str(result[max(result.keys())]) == "Ник")

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.usain, self.andrew, self.nick)
        result = tournament.start()
        self.__class__.all_results["usain_andrew_nick"] = {place: str(runner) for place, runner in result.items()}
        self.assertTrue(str(result[max(result.keys())]) == "Ник")