import runner
import unittest

class RunnerTest(unittest.TestCase):

    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        run_1 = runner.Runner('Vasya')
        for i in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_1 = runner.Runner('Vasya')
        for i in range(10):
            run_1.run()
        self.assertEqual(run_1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_1 = runner.Runner('Vasya')
        run_2 = runner.Runner('Petya')
        for i in range(10):
            run_1.run()
        for j in range(10):
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)