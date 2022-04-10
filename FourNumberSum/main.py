
# Avg: O(n^2)
# Worst: O(n^3) bc we iterate over all pairs in pair_sum_table
# 	- imagine this case: [-4,-3,-2,-1,1,2,3,4]
# 		* we might get {0: [[-4,4], [-3,3]...], ...} in the pair_sum_table

def four_number_sum(array, target_sum):
	n = len(array)
	pair_sum_table = {}
	quadruplets = []

	for i in range(1, n-1):
		for j in range(i+1, n):
			diff = target_sum - (array[i] + array[j])
			if diff in pair_sum_table:
				for pair in pair_sum_table[diff]:
					quadruplets.append(pair + [array[i], array[j]])

		for k in range(0, i):
			curr_sum = (array[i] + array[k])
			if curr_sum not in pair_sum_table:
				pair_sum_table[curr_sum] = [[array[i], array[k]]]
			else:
				pair_sum_table[curr_sum].append([array[i], array[k]])

	return quadruplets


if __name__ == '__main__':
	print(f'\n\n\n')
	import json
	test_cases = json.load(open('test_cases.json', mode='r'))
	for test_case in test_cases:
		input_params = test_case['input']
		result = four_number_sum(input_params['array'], input_params['targetSum'])
