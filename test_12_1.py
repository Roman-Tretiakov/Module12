from runner import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def setUp(self):
        self.runner_tom = Runner('Tom')
        self.runner_petya = Runner('Petya')

    def test_walk(self):
        for _ in range(10):
            self.runner_tom.walk()
        self.assertEqual(50, self.runner_tom.distance,
                         f'test Runner.walk() is failed. Expected: 50, Actual: {self.runner_tom.distance}.')

    def test_run(self):
        for _ in range(10):
            self.runner_tom.run()
        self.assertEqual(100, self.runner_tom.distance,
                         f'test Runner.run() is failed. Expected: 100, Actual: {self.runner_tom.distance}.')

    def test_challenge(self):
        for _ in range(10):
            self.runner_tom.run()
            self.runner_petya.walk()
        self.assertNotEqual(self.runner_tom.distance, self.runner_petya.distance,
                            'test Runner.run() and Runner.walk() is failed. Expected: Not equal, Actual: Equal.')


if __name__ == '__main__':
    unittest.main()
