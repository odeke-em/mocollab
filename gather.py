def gather(transport, unit_list, value):
	"""
	Finds the maximum possible "value" of troops that can be loaded
	in to the remaining space of a transport.

	Input:
	 transport - The transport unit to be loaded.
	 unit_list - The list of units that can be loaded onto transport.
	   You may assume that these units are non-transport ground units
	   that are already on the same team as the transport, have not
	   moved this turn, and can reach the transport with a single move.
	 value - a function that maps a unit to some value

	Output:
	 A list of units from unit_list. Do NOT load them into the transport
	 here, just compute the list of units with maximum possible value whose
	 total size is at most the remaining capacity of the transport.

	 The calling function from gui.py will take care of loading them.

	Target Complexity:
	 It is possible to implement this method to run in time
	 O(n * C) where n is the number of units in unit_list and C
	 is the remaining capacity in the transport. Remember, the capacity
	 of a transport and the sizes of the units are all integers.
	"""
	gathered = list()
	unitSize = list()
	unitValue = list()
	bestUnits = list()
	# the unused capacity of the transport
	remain = transport.capacity
	
	# Finds the number of units available
	numUnits = len(unit_list)
	
	# Declares the array used for dynamic programming
	weights = [[0 for i in range(remain + 1)] for j in range(numUnits +1)]
	# Original code
	"""
	for u in unit_list:
		if u.unit_size <= remain:
			gathered.append(u)
			remain -= u.unit_size
	"""
	
	# Sets up a list for easy access of unit sizes and values
	for u in unit_list:
		x = int(u.unit_size)
		unitSize.append(x)
		y = int(value(u))
		unitValue.append(y)
		
	print(unitValue)
	# Increments through the array checking values against previous values and weights
	for l in range(0, numUnits):
		for k in range(1, remain):
			if unitSize[l] <= k and weights[l-1][k] < weights[l-1][k - unitSize[l]] + unitValue[l]:
				weights[l][k] = weights[l-1][k - unitSize[l]] + unitValue[l]
			else:
				weights[l][k] = weights[l-1][k]
	
	# If the weight is not equal between weights[l][remain] and weights[l-1][remain]
	# Then it is in the solution
	for l in range(numUnits, 0, -1):
		bestWeights = weights[l][remain] != weights[l-1][remain]
		if bestWeights:
			bestUnits.ppend(unitSize[l-1]
	
	# Compares the weights from bestWeights against the weights of the units
	# To see which individual units are in the solution
	for p in unit_list:
		for k in range(0, len(bestUnits)):
			if p.unit_size = bestUnits[k]:
				gathered.append(p)
			
	# referenced pseudo-code for dynamic programming solution at
	# http://en.wikipedia.org/wiki/Knapsack_problem
	
	return gathered

