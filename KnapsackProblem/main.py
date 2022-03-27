
def knapsack_problem(items, capacity):

	counter = 0
	for item in items:
		knapsack_problem_helper(items, capacity, item, curr_item_idx=counter)

def knapsack_problem_helper(items, capacity, curr_item=[], curr_item_idx=0, curr_weight=0):
	if curr_item_idx == 0:


	if curr_weight == capacity:
		return curr_weight, curr_item_idx



	return


print(f'\n\n')
import json
test_cases = json.load(open('test_cases.json'))
for test_case in test_cases:
	knapsack_problem(test_case['inputs']['items'], test_case['inputs']['capacity'])
