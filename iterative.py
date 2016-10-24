def find_child(lst_of_nodes):
	# print "we are currently in this", lst_of_nodes[0][-1]
	if lst_of_nodes[0][-1] == 175:
		# print "at the home base yo, we gucci."
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
		# print "before while loop", lst, "dup length", dup_len
		# print "here's the list of nodes" , lst_of_nodes
		while j <= dup_len:
			# print "currently j", j, "adding this", access_flight[lst_of_nodes[j][-1]].child[j]
			lst[j].append(access_flight[lst_of_nodes[j][-1]].child[j])
			j+=1
		# print "before recursion, our lst", lst
		find_child(lst)

def find_child_iterative(lst_of_nodes):
	while (not not lst_of_nodes):
		if lst_of_nodes[0][-1] == 175:
		# print "at the home base yo, we gucci."
			possible_crews.append(lst_of_nodes.pop(0))
					
		dup_len = len(access_flight[lst_of_nodes[0][-1]].child)-1
		temp = lst_of_nodes[0]
		for i in range(dup_len):
			temp = temp[:]
			lst_of_nodes.insert(0,temp)
		j = 0
		# print "before while loop", lst, "dup length", dup_len
		# print "here's the list of nodes" , lst_of_nodes
		while j <= dup_len:
			# print "currently j", j, "adding this", access_flight[lst_of_nodes[j][-1]].child[j]
			lst_of_nodes[j].append(access_flight[lst_of_nodes[j][-1]].child[j])
			j+=1