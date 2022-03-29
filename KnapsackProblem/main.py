# import sys
# import time
#
# def knapsack_problem(items, capacity):
# 	start_time = time.time()
# 	res = knapsack_problem_helper(items, capacity, len(items)-1)
# 	print(f'exec time: {time.time() - start_time}')
# 	return [res[0], res[1]]

import sys
import time


def knapsack_problem(items, capacity):
	start_time = time.time()
	# res = knapsack_problem_helper(items, capacity, len(items)-1)
	
	matrix = [[-1 for j in range(capacity+1)] for i in range(len(items))]
	print(f'exec time: {time.time() - start_time}')
	return [res[0], res[1]]


def knapsack_problem_helper(items, capacity, idx):
	if capacity == 0 or idx == -1:
		return [0, []]

	if items[idx][1] <= capacity:
		res_with_item = knapsack_problem_helper(items, capacity-items[idx][1], idx-1)
		res_with_item[0] += items[idx][0]
		res_with_item[1].append(idx)

		res_without_item = knapsack_problem_helper(items, capacity, idx-1)

		return res_with_item if res_with_item[0] > res_without_item[0] else res_without_item
	else:
		res_without_item = knapsack_problem_helper(items, capacity, idx-1)
		return res_without_item


def knapsack_problem_helper_memoization(items, capacity, idx):
    
    
	if capacity == 0 or idx == -1:
		return [0, []]

	if items[idx][1] <= capacity:
		res_with_item = knapsack_problem_helper(items, capacity-items[idx][1], idx-1)
		res_with_item[0] += items[idx][0]
		res_with_item[1].append(idx)

		res_without_item = knapsack_problem_helper(items, capacity, idx-1)

		return res_with_item if res_with_item[0] > res_without_item[0] else res_without_item
	else:
		res_without_item = knapsack_problem_helper(items, capacity, idx-1)
		return res_without_item



# def knapsack_problem_helper_tuples(items, capacity, idx):
# 	if capacity == 0 or idx == -1:
# 		return 0, []

# 	if items[idx][1] <= capacity:
# 		res_with_item_temp = knapsack_problem_helper_tuples(items, capacity-items[idx][1], idx-1)
# 		res_with_item_temp[1].append(idx)
# 		res_with_item = (items[idx][0] + res_with_item_temp[0]), res_with_item_temp[1]

# 		res_without_item = knapsack_problem_helper_tuples(items, capacity, idx-1)

# 		return res_with_item if res_with_item[0] > res_without_item[0] else res_without_item
# 	else:
# 		res_without_item = knapsack_problem_helper_tuples(items, capacity, idx-1)
# 		return res_without_item


print(f'\n\n')
import json
test_cases = json.load(open('test_cases.json'))
test_case = test_cases[0]
print(knapsack_problem(test_case['inputs']['items'], test_case['inputs']['capacity']))
# for test_case in test_cases:
# 	print(knapsack_problem(test_case['inputs']['items'], test_case['inputs']['capacity']))
