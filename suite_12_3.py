import unittest
import tests_12_1
import tests_12_2

runnerTS = unittest.TestSuite()
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
runnerTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

run = unittest.TextTestRunner(verbosity=2)
run.run(runnerTS)