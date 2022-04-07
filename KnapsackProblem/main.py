
def knapsack_problem(items, capacity):
	# memo = [[-1 for j in range(capacity+1)] for i in range(len(items)+1)]		# needed for memoization func
	res = knapsack_problem_iterative_tabulation(items, capacity)
	return res


def knapsack_problem_recursive(items, capacity, idx):
	if capacity == 0 or idx == -1:
		return [0, []]

	if items[idx][1] <= capacity:
		res_with_item = knapsack_problem_recursive(items, capacity-items[idx][1], idx-1)
		res_with_item[0] += items[idx][0]
		res_with_item[1].append(idx)																						# appends add O(len(arr1) + len(arr2))

		res_without_item = knapsack_problem_recursive(items, capacity, idx-1)

		return res_with_item if res_with_item[0] > res_without_item[0] else res_without_item
	else:
		res_without_item = knapsack_problem_recursive(items, capacity, idx-1)
		return res_without_item


def knapsack_problem_memoization(items, capacity, item_idx, memo):

	if memo[item_idx][capacity] != -1:
		return memo[item_idx][capacity]

	if capacity == 0 or item_idx == 0:
		return [0, []]

	if items[item_idx-1][1] <= capacity:
		# added temp var to avoid editing object in memo
		res_with_item_temp = knapsack_problem_memoization(items, capacity-items[item_idx-1][1], item_idx-1, memo)
		res_with_item = [res_with_item_temp[0]+items[item_idx-1][0], res_with_item_temp[1] + [item_idx-1]]					# appends add O(len(arr1) + len(arr2))

		res_without_item = knapsack_problem_memoization(items, capacity, item_idx-1, memo)

		memo[item_idx][capacity] = res_with_item if res_with_item[0] > res_without_item[0] else res_without_item
		return memo[item_idx][capacity]
	else:
		memo[item_idx][capacity] = knapsack_problem_memoization(items, capacity, item_idx-1, memo)
		return memo[item_idx][capacity]


def knapsack_problem_iterative_tabulation(items, capacity):
	memo = [[[0, []] if i == 0 or j == 0 else None for j in range(capacity+1)] for i in range(len(items)+1)]
	for i in range(1, len(items)+1):
		current_value = items[i-1][0]
		current_weight = items[i-1][1]
		for j in range(1, capacity+1):
			if current_weight <= j:
				updated_value_items = [(current_value + memo[i-1][j-current_weight][0]),
									   (memo[i-1][j-current_weight][1] + [i-1])]
				without_item = memo[i-1][j]
				memo[i][j] = updated_value_items if updated_value_items[0] > without_item[0] else without_item
			else:
				memo[i][j] = memo[i-1][j]
	return memo[len(items)][capacity]


# print(f'\n\n')
# import json
# test_cases = json.load(open('test_cases.json'))
# for test_case in test_cases:
# 	print(test_case['input'])
# 	output = knapsack_problem(test_case['input']['items'], test_case['input']['capacity'])
# 	print(f'\t{output}')
# 	if output == test_case['expected_output']:
# 		print(f'\tPassed')
