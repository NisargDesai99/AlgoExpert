import sys


def knapsack_problem(items, capacity):

	values = []

	counter = 0
	for item in items:
		values.append(knapsack_problem_helper(items, capacity, [], curr_item_idx=counter))
		print(f'values: {values}')
		counter += 1

	# find max value from values list
	max = -sys.maxsize - 1
	max_idx = -1
	max_idx = 0		# update to correct item after
	return items[max_idx]


def knapsack_problem_helper(items, capacity, items_in_bag=None, curr_item_idx=0, curr_weight=0, curr_value=0):
	if items_in_bag is None:
		items_in_bag = []

	if curr_weight == capacity or curr_item_idx >= len(items):
		return curr_value, items_in_bag

	if (curr_weight + items[curr_item_idx][1]) <= capacity:
		items_in_bag.append(curr_item_idx)
		return items[curr_item_idx][0] + knapsack_problem_helper(items, capacity,
																 items_in_bag,
																 curr_item_idx+1,
																 curr_weight+items[curr_item_idx][1])[0], items_in_bag
	else:
		return knapsack_problem_helper(items, capacity,
									   items_in_bag,
									   curr_item_idx+1,
									   curr_weight)[0], items_in_bag

	print(f'a')


print(f'\n\n')
import json
test_cases = json.load(open('test_cases.json'))
test_case = test_cases[0]
print(knapsack_problem(test_case['inputs']['items'], test_case['inputs']['capacity']))
# for test_case in test_cases:
# 	print(knapsack_problem(test_case['inputs']['items'], test_case['inputs']['capacity']))
