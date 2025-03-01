import unittest
import math
from savprogram.asearch import a_star_search, is_valid

class TestAStarSearch(unittest.TestCase):

    def setUp(self):
        """Set up a simple grid for testing."""
        self.grid = [
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
        ]
        self.src = (0, 0)  # Start point
        self.dest = (8, 9)  # End point

    def test_a_star_search_basic(self):
        """Test A* search on a simple grid."""
        path = a_star_search(self.grid, self.src, self.dest)

        # Ensure that the path is valid (list of tuples)
        self.assertIsInstance(path, list)
        self.assertTrue(all(isinstance(x, tuple) and len(x) == 2 for x in path))

        # Check if the start and destination are in the path
        self.assertEqual(path[0], self.src)
        self.assertEqual(path[-1], self.dest)

        # Check if the path is valid (i.e., no cell in the path is blocked)
        for cell in path:
            x, y = cell
            self.assertTrue(is_valid(x, y, self.grid))

    def test_a_star_search_no_path(self):
        """Test A* search when no path exists due to blocking cells."""
        blocked_grid = [
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
        ]
        src = (0, 0)
        dest = (8, 9)

        with self.assertRaises(ValueError) as context:
            a_star_search(blocked_grid, src, dest)

        self.assertEqual(str(context.exception), "Failed to find a path to the destination.")

    def test_a_star_search_invalid_start_or_dest(self):
        """Test A* search with invalid start or destination points."""
        invalid_grid = [
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ]
        invalid_src = (-1, 0)
        invalid_dest = (3, 3)

        with self.assertRaises(ValueError) as context:
            a_star_search(invalid_grid, invalid_src, invalid_dest)

        self.assertEqual(str(context.exception), "Source or destination is invalid or blocked.")

    def test_a_star_search_small_grid(self):
        """Test A* search on a small grid."""
        small_grid = [
            [1, 1],
            [0, 1]
        ]
        src = (0, 0)
        dest = (1, 1)

        path = a_star_search(small_grid, src, dest)

        # Check if the start and destination are in the path
        self.assertEqual(path[0], src)
        self.assertEqual(path[-1], dest)

if __name__ == '__main__':
    unittest.main()
