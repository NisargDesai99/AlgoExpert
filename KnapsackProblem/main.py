
def knapsack_problem(items, capacity):
	# print(f'{items} | {capacity}')
	return


print(f'\n\n')
import json
test_cases = json.load(open('test_cases.json'))
for test_case in test_cases:
	knapsack_problem(test_case['inputs']['items'], test_case['inputs']['capacity'])
