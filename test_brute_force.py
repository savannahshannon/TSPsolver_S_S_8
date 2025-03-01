import unittest
import time
import random
from savprogram.bruteforce import tsp_brute_force, total_distance

class TestTSPBruteForce(unittest.TestCase):

    def setUp(self):
        """Set up some sample points for testing."""
        self.points = [
            (0, 0),  # Point 1
            (1, 0),  # Point 2
            (1, 1),  # Point 3
            (0, 1),  # Point 4
        ]

    def test_tsp_brute_force_basic(self):
        """Test the brute force TSP function on a small set of points."""
        best_route, min_distance, execution_time = tsp_brute_force(self.points)

        # Check if the result is a valid route (it should be a tuple of indices)
        self.assertEqual(len(best_route), len(self.points))
        self.assertTrue(all(isinstance(x, int) for x in best_route))
        self.assertTrue(all(x >= 0 and x < len(self.points) for x in best_route))

        # Check if the min_distance is a non-negative number
        self.assertGreaterEqual(min_distance, 0)

        # Check if the execution time is reasonable (since brute force can be slow)
        self.assertLess(execution_time, 5)  # Allowing up to 5 seconds for small test cases

    def test_tsp_brute_force_single_point(self):
        """Test the case where there is only one point."""
        single_point = [(0, 0)]
        best_route, min_distance, execution_time = tsp_brute_force(single_point)

        # The best route should be [0], as there is only one point
        self.assertEqual(best_route, (0,))
        self.assertEqual(min_distance, 0)
        self.assertGreater(execution_time, 0)  # Time should be greater than 0, even if it's trivial

    def test_tsp_brute_force_large_input(self):
        """Test the brute force function with a larger set of points."""
        random_points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(6)]  # 6 points
        best_route, min_distance, execution_time = tsp_brute_force(random_points)

        # Ensure that the best route and min_distance are valid
        self.assertEqual(len(best_route), len(random_points))
        self.assertGreaterEqual(min_distance, 0)

        # The execution time should be greater than a trivial test but still reasonable
        self.assertGreater(execution_time, 0)
        self.assertLess(execution_time, 30)  # Allow up to 30 seconds for a larger test

if __name__ == '__main__':
    unittest.main()
