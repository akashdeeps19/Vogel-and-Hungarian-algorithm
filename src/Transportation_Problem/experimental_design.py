from random import uniform

costs_list=[]
demand_list=[]
supply_list=[]
for nd in [20,40,60,100]:
	for deg in [1,2,5,10]:
		for cost in [20,100,500,1000]:
			for instance in range(10):

				ns=10
				x=500 - cost/2 
				y= 500 + cost/2 
				l=[[] for _ in range(ns)]
				for i in range(ns):
					for j in range(nd):
						l[i].append(int(uniform(x,y)))

				demand1= [ int(uniform(75,125)) for _ in range(nd)]
				mean_supply=int ( (deg * (100*nd)*1.0) /10) 
				supply1= [int(uniform(0.75 * mean_supply, 1.25* mean_supply)) for _ in range(ns)]
				ed=False
				es=False
				if sum(supply1)>sum(demand1):
					demand1.append(sum(supply1)-sum(demand1))
					ed=True
				elif sum(supply1)<sum(demand1):
					supply1.append(sum(demand1)-sum(supply1))
					es=True
				supply={}
				demand={}
				for i in range(len(demand1)):
					s="D"+str(i+1)
					demand[s]=demand1[i]

				for i in range(len(supply1)):
					s="S"+str(i+1)
					supply[s]=supply1[i]
				costs={}

				for i in range(ns):
					s="S"+str(i+1)
					dic={}
					for j in range(nd):
						s2="D"+str(j+1)
						dic[s2]=l[i][j] 
					if ed==True:
						dic["D" + str(nd+1)]=0
					costs[s]=dic
				if(es==True):
					s="S"+str(ns+1)
					dic={}
					for j in range(nd):
						s2="D"+str(j+1)
						dic[s2]=0 
					costs[s]=dic

				# print("costs = " , costs)
				# print("demand =", demand)
				# print("supply = ", supply)
				costs_list.append(costs)
				demand_list.append(demand)
				supply_list.append(supply)


import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,costs_list,demand_list,supply_list]
export_data = zip_longest(*d, fillvalue = '')
with open('input.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Instance","Costs","Demand","Supply"))
      wr.writerows(export_data)
myfile.close()