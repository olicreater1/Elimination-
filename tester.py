import unittest
from elimination import solve_system_of_equations

class TestSolveSystemOfEquations(unittest.TestCase):
    def testNoSolution(self):
        a1, b1, c1 = 1, -3, 7
        a2, b2, c2 = 2, -6, 12
        x, y = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
        self.assertEqual(x, "No Solutions")
        self.assertEqual(y, "No Solutions")
    def testInfiniteSolutions(self):
        a1, b1, c1 = 1, 1, 1
        a2, b2, c2 = 2, 2, 2
        x, y = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
        self.assertEqual(x, "Infinitely Many Solutions")
        self.assertEqual(y, "Infinitely Many Solutions")
    def test_unique_solution(self):
        a1, b1, c1 = 2, 3, 6
        a2, b2, c2 = 4, 6, 12
        x, y = solve_system_of_equations(a1, b1, c1, a2, b2, c2)
        self.assertEqual(x, 0.0)
        self.assertEqual(y, 2.0)
    
    def test_zero_division(self):
        a1, b1, c1 = 1, 1, 1
        a2, b2, c2 = 0, 0, 0
        with self.assertRaises(ValueError):
            solve_system_of_equations(a1, b1, c1, a2, b2, c2)
if __name__ == '__main__':
    unittest.main()