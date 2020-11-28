import Assignment_Problem.ap as ap
from Transportation_Problem.Russel_approx_method import Russel
from Transportation_Problem.Vogel_approx_method import  Vogel

if __name__ == "__main__":
	ap.main(10)
	print()
	print()
	costs  = {'W': {'A': 16, 'B': 16, 'C': 13, 'D': 22, 'E': 17},
		  'X': {'A': 14, 'B': 14, 'C': 13, 'D': 19, 'E': 15},
		  'Y': {'A': 19, 'B': 19, 'C': 20, 'D': 23, 'E': 50},
		  'Z': {'A': 50, 'B': 12, 'C': 50, 'D': 15, 'E': 11}}
	demand = {'A': 30, 'B': 20, 'C': 70, 'D': 30, 'E': 60}
	supply = {'W': 50, 'X': 60, 'Y': 50, 'Z': 50}

	print("Vogel Approximation Method")
	obj = Vogel()
	obj.solve(costs,demand,supply , True,False )

	print()
	print()

	costs  = {'W': {'A': 16, 'B': 16, 'C': 13, 'D': 22, 'E': 17},
		  'X': {'A': 14, 'B': 14, 'C': 13, 'D': 19, 'E': 15},
		  'Y': {'A': 19, 'B': 19, 'C': 20, 'D': 23, 'E': 50},
		  'Z': {'A': 50, 'B': 12, 'C': 50, 'D': 15, 'E': 11}}
	demand = {'A': 30, 'B': 20, 'C': 70, 'D': 30, 'E': 60}
	supply = {'W': 50, 'X': 60, 'Y': 50, 'Z': 50}
	print("Russel Approximation Method")

	Russel = Russel()
	Russel.solve(costs,demand,supply,True,False)




