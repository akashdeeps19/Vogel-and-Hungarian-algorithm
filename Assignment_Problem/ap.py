import Assignment_Problem.hungarian as hungarian
import Assignment_Problem.naive_algo as naive_algo
import random
import time

def matrix_generator(n, start = 0, end = 1000):
    return [[random.randint(start, end) for __ in range(n)] for _ in range(n)]

def main(size):
    cost_matrix = matrix_generator(size)
    print("Started exhaustive search...\n")
    start = time.time()
    n_cost = naive_algo.min_cost(cost_matrix)
    n_time = time.time() - start

    print("Started Hungarian Algorithm...\n")
    start = time.time()
    hung = hungarian.Hungarian(cost_matrix)
    hung.solve()
    h_cost = hung.totalPotential
    h_time = time.time() - start
    print(f"Matrix size = {size} x {size}")
    print(f"Minimum cost by exhaustive search using naive algorithm = {n_cost}")
    print(f"Minimum cost using Hungarian algorithm = {h_cost}\n")
    print(f"Time required for  exhaustive search using naive algorithm = {n_time}s")
    print(f"Time required for Hungarian algorithm = {h_time}s\n")

    mat = [[90, 75, 75, 80],
        [35, 85, 55, 65],
        [125, 95, 90, 105],
        [45, 110, 95, 115]]
    
    row_names = ['1', '2', '3' ,'4']
    col_names = ['A', 'B', 'C', 'D']

    print("For the cost matrix")
    print(end = '  \t')
    for col in col_names:
        print(f"{col}", end = '\t')
    print()

    for i,row in enumerate(mat):
        print(f"{row_names[i]}  |", end = '\t')
        for e in row:
            print(e, end = '\t')
        print('|')

    h = hungarian.Hungarian(mat)
    h.solve()
    print(f"\nMinimum cost using Hungarian Problem = {h.totalPotential}")
    print("Assignments are as follows")
    for (i,j) in h.results:
        print(f"{row_names[i]} - {col_names[j]}")

if __name__ == "__main__":
    main(5)