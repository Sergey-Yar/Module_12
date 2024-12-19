import runner_and_tournament as r_a_t
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = r_a_t.Runner('Усэйн', 10)
        self.runner_2 = r_a_t.Runner('Андрей', 9)
        self.runner_3 = r_a_t.Runner('Ник', 3)


    def test_start_1(self):
        tournament = r_a_t.Tournament(90, self.runner_1, self.runner_3)
        self.all_results = tournament.start()
        last_finish_time = max(self.all_results.keys())
        self.assertTrue(self.all_results[last_finish_time] == 'Ник')
        type(self).all_results.update(self.all_results)

    def test_start_2(self):
        tournament = r_a_t.Tournament(90, self.runner_2, self.runner_3)
        self.all_results = tournament.start()
        last_finish_time = max(self.all_results.keys())
        self.assertTrue(self.all_results[last_finish_time] == 'Ник')
        type(self).all_results.update(self.all_results)

    def test_start_3(self):
        tournament = r_a_t.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results = tournament.start()
        last_finish_time = max(self.all_results.keys())
        self.assertTrue(self.all_results[last_finish_time] == 'Ник')
        type(self).all_results.update(self.all_results)

    @classmethod
    def tearDown(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

