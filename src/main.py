import Assignment_Problem.ap as ap
from Transportation_Problem.Russel_approx_method import Russel
from Transportation_Problem.Vogel_approx_method import  Vogel
import random
import pandas as pd
import copy

if __name__ == "__main__":
	ap.main(9)
	print()
	print()

	costs  = {'W': {'A': random.randint(10,99), 'B': random.randint(10,99), 'C': random.randint(10,99), 'D': random.randint(10,99), 'E': random.randint(10,99)},
		  'X': {'A': random.randint(10,99), 'B': random.randint(10,99), 'C':random.randint(10,99), 'D': random.randint(10,99), 'E':random.randint(10,99)},
		  'Y': {'A': random.randint(10,99), 'B': random.randint(10,99), 'C': random.randint(10,99), 'D': random.randint(10,99), 'E': random.randint(10,99)},
		  'Z': {'A': random.randint(10,99), 'B': random.randint(10,99), 'C': random.randint(10,99), 'D': random.randint(10,99), 'E': random.randint(10,99)}}
	demand = {'A': 30, 'B': 20, 'C': 70, 'D': 30, 'E': 60}
	supply = {'W': 50, 'X': 60, 'Y': 50, 'Z': 50}

	costs1=copy.deepcopy(costs)
	print("Vogel Approximation Method")
	obj = Vogel()
	obj.solve(costs,demand,supply,True,False)

	print()
	print()

	demand = {'A': 30, 'B': 20, 'C': 70, 'D': 30, 'E': 60}
	supply = {'W': 50, 'X': 60, 'Y': 50, 'Z': 50}
	print("Russel Approximation Method")

	Russel = Russel()
	Russel.solve(costs1,demand,supply,True,False)




