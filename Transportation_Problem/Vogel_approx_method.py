import pandas as pd 
from collections import defaultdict
import math
import copy
import json
import ast

class Vogel:

	def solve(self,costs,demand,supply,to_print=False , tocm=False):
		res = dict((k, defaultdict(int)) for k in costs)
		g = {}
		costs1=copy.deepcopy(costs)
		costs2=copy.deepcopy(costs)
		costs3=copy.deepcopy(costs)
		cols = sorted(demand.keys())
		supply1 = copy.deepcopy(supply)
		demand1=copy.deepcopy(demand)
		if tocm==True:
			for i in supply:
				mi=min(costs[i].values())
				for j in costs2[i]:
					costs2[i][j]-=mi
				# print(costs2)
			for i in demand :
				mi=10000
				for j in supply:
					if costs[j][i]<mi :
						mi=costs[j][i]
				for j in supply:
					costs3[j][i]=costs3[j][i]-mi 
				# print(costs3)

			for i in demand:
				for j in supply:
					costs[j][i]= costs2[j][i]+costs3[j][i]
		for x in supply:
			g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
		for x in demand:
			g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])
		while g:
			d = {}
			# print(supply,demand)
			for x in demand:
				d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else (costs[g[x][0]][x])
			s = {}
			for x in supply:
				s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]])  if len(g[x]) > 1 else costs[x][g[x][0]]
			f = max(d, key=lambda n: d[n])
			t = max(s, key=lambda n: s[n])
			t, f = (f, g[f][0]) if d[f] >= s[t] else (g[t][0], t)
			v = min(supply[f], demand[t])
			# print(f,t)
			# print(v)
			res[f][t] += v
			demand[t] -= v
			
			if demand[t] == 0:
				for k, n in supply.items():
					if n != 0:
						g[k].remove(t)
				del g[t]
				del demand[t]
			supply[f] -= v
			if supply[f] == 0:
				for k, n in demand.items():
					if n != 0:
						g[k].remove(f)
				del g[f]
				del supply[f]
			# print("G",g)
		cost = 0

		if to_print==True:
			print("Cost Matrix:")
			print(" ", end= "    ")
			for col in cols:
				print(col , end="    ")
			print("Supply")
			print()

			for g in sorted(costs):
				print (g, end="   ")
				for n in cols:
					print(costs1[g][n] , end="   ")
				print(supply1[g])
				# print()

			print("Dem" , end=" ")
			for n in cols:
				print(demand1[n] , end="   ")

			print()
			print()


		if to_print==True:
			print("Assignmnet Matrix")
			print(" ", end= "    ")
			for col in cols:
				print(col , end="    ")
			print()


		for g in sorted(costs):
			if to_print:
				print (g, end="   ")
			for n in cols:
				y = res[g][n]
				if True:
					# pass
					cost += y * costs1[g][n]

					if to_print:
						if y==0:
							y="0 "
						print (y,end="   ")
					
					# print ("  ",)
			if to_print:
				print()

		if to_print:
			print("Total cost =",cost)
		return cost

if __name__ == "__main__": 
	costs  = {'W': {'A': 16, 'B': 16, 'C': 13, 'D': 22, 'E': 17},
		  'X': {'A': 14, 'B': 14, 'C': 13, 'D': 19, 'E': 15},
		  'Y': {'A': 19, 'B': 19, 'C': 20, 'D': 23, 'E': 50},
		  'Z': {'A': 50, 'B': 12, 'C': 50, 'D': 15, 'E': 11}}
	demand = {'A': 30, 'B': 20, 'C': 70, 'D': 30, 'E': 60}
	supply = {'W': 50, 'X': 60, 'Y': 50, 'Z': 50}
	obj = Vogel()
	obj.solve(costs,demand,supply , True,False )