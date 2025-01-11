import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Alice")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

if name == 'main':
    unittest.main()