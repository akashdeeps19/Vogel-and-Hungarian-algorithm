from itertools import permutations 
import math


def min_cost(mat):
    l = permutations(range(len(mat)))
    cost = math.inf
    while(1):
        try:
            curr = sum([mat[idx][m] for idx,m in enumerate(l.__next__())])
            cost = min(cost, curr)
        except:
            break
    return cost

if __name__ == "__main__":
    mat = [[90, 75, 75, 80],
       [35, 85, 55, 65],
       [125, 95, 90, 105],
       [45, 110, 95, 115]]
       
    print(min_cost(mat))
