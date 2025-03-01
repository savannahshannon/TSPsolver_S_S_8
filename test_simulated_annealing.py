import unittest
import random
from savprogram.simulatedannealing import simulated_annealing, total_distance

class TestSimulatedAnnealing(unittest.TestCase):

    def setUp(self):
        """Set up some sample points for testing."""
        self.points = [
            (0, 0),  # Point 1
            (1, 0),  # Point 2
            (1, 1),  # Point 3
            (0, 1),  # Point 4
        ]

    def test_simulated_annealing_basic(self):
        """Test the simulated annealing function on a small set of points."""
        best_tour, best_distance = simulated_annealing(self.points)

        # Check if the result is a valid tour (it should be a list of indices)
        self.assertEqual(len(best_tour), len(self.points))
        self.assertTrue(all(isinstance(x, int) for x in best_tour))
        self.assertTrue(all(x >= 0 and x < len(self.points) for x in best_tour))

        # Check if the best_distance is a non-negative number
        self.assertGreaterEqual(best_distance, 0)

    def test_simulated_annealing_single_point(self):
        """Test the case where there is only one point."""
        single_point = [(0, 0)]
        with self.assertRaises(ValueError):
            simulated_annealing(single_point)

    def test_simulated_annealing_works_with_large_number_of_points(self):
        """Test the algorithm on a larger number of points."""
        random_points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(100)]
        best_tour, best_distance = simulated_annealing(random_points)

        # Ensure that the best tour is valid
        self.assertEqual(len(best_tour), len(random_points))
        self.assertGreaterEqual(best_distance, 0)

if __name__ == '__main__':
    unittest.main()
