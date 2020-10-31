from Russel_approx_method import Russel
from Vogel_approx_method import Vogel 
import ast
import pandas as pd
import copy
data= pd.read_csv('input.csv')

Russel = Russel()
Vogel = Vogel()

vogel=[]
vogel_tocm=[]
russel=[]
russel_tocm=[]
ranks = []
for instance in range(640):
	print(instance+1)
	l=[]
	costs1=ast.literal_eval(data['Costs'].iloc[instance])
	demand1=ast.literal_eval(data['Demand'].iloc[instance])
	supply1=ast.literal_eval(data['Supply'].iloc[instance])

	costs,demand,supply= copy.deepcopy(costs1) , copy.deepcopy(demand1) , copy.deepcopy(supply1)
	vg = Vogel.solve(costs,demand,supply,False,False)
	vogel.append(vg)
	l.append(vg)

	costs,demand,supply= copy.deepcopy(costs1) , copy.deepcopy(demand1) , copy.deepcopy(supply1)
	vg_tocm = Vogel.solve(costs,demand,supply,False,True)
	vogel_tocm.append(vg_tocm)
	l.append(vg_tocm)

	costs,demand,supply= copy.deepcopy(costs1) , copy.deepcopy(demand1) , copy.deepcopy(supply1)
	rs = Russel.solve(costs,demand,supply,False,False)
	russel.append(rs)
	l.append(rs)

	costs,demand,supply= copy.deepcopy(costs1) , copy.deepcopy(demand1) , copy.deepcopy(supply1)
	rs_tocm = Russel.solve(costs,demand,supply,False,True)
	russel_tocm.append(rs_tocm)
	l.append(rs_tocm)

	o= [(sorted(l).index(x)+1) for x in l]
	# print(l)
	# print(o)
	ranks.append(o)
	# break


iranks=[[0 for _ in range (4)] for _ in range(4)]


for algo in range(4):

	for rank in range(1,5):
		num=0
		for i in range(640):
			if ranks[i][algo]==rank:
				num+=1
		iranks[algo][rank-1]=num

integrated_ranks=[0 for _ in range(4)]

for algo in range(4):

	integrated_ranks[algo] = (iranks[algo][0] + iranks[algo][1]*2 + iranks[algo][2]*3 + iranks[algo][3]*4)/640

print(iranks)

print(integrated_ranks)




import csv
from itertools import zip_longest
instance_number=range(1,641)
d = [instance_number,vogel , vogel_tocm , russel , russel_tocm]
export_data = zip_longest(*d, fillvalue = '')
with open('Results.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
	  wr = csv.writer(myfile)
	  wr.writerow(("Instance","Vogel","Vogel-TOCM", "Russel", "Russel-TOCM"))
	  wr.writerows(export_data)
myfile.close()

# Output
# [[86, 163, 227, 164], [211, 47, 348, 34], [148, 242, 116, 134], [235, 154, 150, 101]]
# [2.7328125, 2.3203125, 2.36875, 2.1828125]