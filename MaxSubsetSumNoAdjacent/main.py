# dynamic programming

# O(n) time - iterating over input array
# O(n) space - from max_sums array
def max_subset_sum_no_adjacent_On_space(array):
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]

	# copy the given array to max sums to initialize it
	# set max_sums[1] to the max of 0 and 1 indices
	max_sums = array[:]
	max_sums[1] = max(array[0], array[1])

	for i in range(2, len(array)):
		max_sums[i] = max(max_sums[i-1], max_sums[i-2] + array[i])
		print(f'i = {i}; max_sums = {max_sums}')

	return max_sums[-1]


# O(n) time - iterating over input array
# O(1) space - only track two variables since we only need i-1 and i-2 max sums
def max_subset_sum_no_adjacent(array):
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]

	second = array[0]					# the i-2 value
	first = max(array[0], array[1])		# the i-1 value

	for i in range(2, len(array)):
		current_max = max(first, second + array[i])
		second = first			# move "pointers" forward
		first = current_max

	return first
