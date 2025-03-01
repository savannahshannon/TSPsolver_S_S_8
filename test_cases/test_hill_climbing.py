import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from savprogram.hillclimbing import hill_climbing

class TestHillClimbing(unittest.TestCase):
    def test_quadratic_function(self):
        """Test hill climbing with a quadratic function."""
        def f(x):
            return -(x - 3) ** 2 + 9  # Maximum at x = 3

        x0 = 0  # Starting point
        x_optimal, f_max = hill_climbing(f, x0)

        self.assertEqual(x_optimal, 3)
        self.assertEqual(f_max, f(3))

    def test_plateau(self):
        """Test hill climbing with a plateau function."""
        def f(x):
            return 10 if 2 <= x <= 4 else x  # Plateau from x=2 to x=4

        x0 = 0  # Start outside the plateau
        x_optimal, f_max = hill_climbing(f, x0)

        self.assertIn(x_optimal, [2, 3, 4])  # Should end up on the plateau
        self.assertEqual(f_max, 10)

    def test_multiple_peaks(self):
        """Test hill climbing with multiple peaks."""
        def f(x):
            peaks = {2: 5, 5: 10, 8: 7}
            return peaks.get(x, 0)  # Multiple peaks at x=2, x=5, and x=8

        x0 = 1  # Start near x=2
        x_optimal, f_max = hill_climbing(f, x0)

        self.assertEqual(x_optimal, 5)  # Should find the highest peak at x=5
        self.assertEqual(f_max, 10)

if __name__ == "__main__":
    unittest.main()
