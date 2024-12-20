import logging
import rt_with_exceptions as runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            run_1 = runner.Runner('Vasya', -5)
            for i in range(10):
                run_1.walk()
            self.assertEqual(run_1.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            run_1 = runner.Runner(25)
            for i in range(10):
                run_1.run()
            self.assertEqual(run_1.distance, 100)
            logging.info('test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_1 = runner.Runner('Vasya')
        run_2 = runner.Runner('Petya')
        for i in range(10):
            run_1.run()
        for j in range(10):
            run_2.walk()
        self.assertNotEqual(run_1.distance, run_2.distance)

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(asctime)s / %(levelname)s / %(message)s')
