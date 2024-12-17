import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run_1 = runner.Runner('Vasya')
        for i in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    def test_run(self):
        run_1 = runner.Runner('Vasya')
        for i in range(10):
            run_1.run()
        self.assertEqual(run_1.distance, 100)

    def test_challenge(self):
        run_1 = runner.Runner('Vasya')
        run_2 = runner.Runner('Petya')
        for i in range(10):
            run_1.run()
        for j in range(10):
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)