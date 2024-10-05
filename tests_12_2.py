import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = rt.Runner('Усэйн', 10)
        self.runner_2 = rt.Runner('Андрей', 9)
        self.runner_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(*cls.all_results, sep='\n')

    def test_tournament_1(self):
        _tournament = rt.Tournament(90, self.runner_1, self.runner_3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner_3.name)

    def test_tournament_2(self):
        _tournament = rt.Tournament(90, self.runner_2, self.runner_3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner_3.name)

    def test_tournament_3(self):
        _tournament = rt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.append(_tournament.start())
        index = len(self.all_results[-1])

        self.assertTrue(self.all_results[-1][index] == self.runner_3.name)

    # Дополнительный тест на правильное расположение бегунов в забегах:
    def test_tournaments(self):
        exp_results_tournament = [{1: self.runner_1.name, 2: self.runner_3.name}, {1: self.runner_2.name,
            2: self.runner_3.name}, {1: self.runner_1.name, 2: self.runner_2.name, 3: self.runner_3.name}]

        self.assertEqual(self.all_results, exp_results_tournament)
