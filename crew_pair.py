import pandas as pd
df=pd.read_csv('flightdata.csv',header=None)

class Node:
	def __init__(self, num=None, child=None):
		self.num = num
		self.child = []
	def add_node(self, num):
		self.child.append(num)

a0=Node(0)
a1=Node(1)
a2=Node(2)
a3=Node(3)
a4=Node(4)
a5=Node(5)
flights = [a0,a1,a2,a3,a4]
access_flight = {0 : a0, 1 : a1, 2 : a2, 3 : a3, 4 : a4, 5: a5}
for node in flights: #for all flights that's not in the dummy
	flight_num = node.num
	print flight_num
	print node.child
	for j, val in df.iterrows():
		idx = 0
		for feasible in val:
			idx +=1
			print "flight: ", j, "feasible", feasible
			if feasible==1 and flight_num==j:
				node.add_node(int(idx))

possible_crews = [] #all possible crews
lst = [[0]] #head
def find_child(lst_of_nodes):
	print "we are currently in this", lst_of_nodes[0][-1]
	if lst_of_nodes[0][-1] == 5:
		print "at the home base yo, we gucci."
		possible_crews.append(lst_of_nodes.pop(0))
		if lst:
			find_child(lst)
		# possible_crews.append(all_paths)
	else:
		dup_len = len(access_flight[lst_of_nodes[0][-1]].child)-1
		temp = lst[0]
		for i in range(dup_len):
			temp = temp[:]
			lst.insert(0,temp)
		j = 0
		print "before while loop", lst, "dup length", dup_len
		print "here's the list of nodes" , lst_of_nodes
		while j <= dup_len:
			print "currently j", j, "adding this", access_flight[lst_of_nodes[j][-1]].child[j]
			lst[j].append(access_flight[lst_of_nodes[j][-1]].child[j])
			j+=1
		print "before recursion, our lst", lst
		find_child(lst)

find_child(lst)

def find_crews(possible_crews, visited, crew):
	i=0
	while i<len(possible_crews):
		add = True
		for visit in visited:
			if visit in possible_crews[i]:
				add = False
				break
		if add:
			crew.append(possible_crews[i])
			for flight in possible_crews[i]:
				if flight not in [0,5]:
					visited.append(flight)
		i += 1

solution = {}
sol_num = 1
possible_crews = sorted(possible_crews, key=len)
visited = [-1]
crew = []
i = len(possible_crews)
while i >=1:
	i -= 1
	visited = [-1]
	crew = []
	temp = possible_crews[i:]+possible_crews[:i]
	find_crews(temp, visited, crew)
	print visited, crew
	if len(visited) == 5:
		crew.sort()
		add=True
		for key in solution:
			add=True
			if crew == solution[key]:
				add=False
				break
		if add:
			solution[sol_num] = crew
			sol_num += 1











