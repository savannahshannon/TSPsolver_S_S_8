from .savprogram.asearch import a_star_search
from .savprogram.bruteforce import tsp_brute_force
from .savprogram.hillclimbing import hill_climbing
from .savprogram.simulatedannealing import simulated_annealing
        
cities = [(0, 0), (2, 3), (5, 4), (6, 1), (8, 3), (1, 6)]
        
print("Random Search:", a_star_search(cities, iterations=1000))
print("Hill Climbing:", hill_climbing(cities))
print("Brute Force:", tsp_brute_force(cities))
print("Simulated Annealing:", simulated_annealing(cities, temp=1000, cooling_rate=0.995))