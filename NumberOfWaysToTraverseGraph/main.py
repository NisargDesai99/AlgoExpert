

def num_ways_to_traverse_graph(width, height, curr_row=0, curr_col=0):
	print(f'{curr_row}: {height}')
	print(f'{curr_col}: {width}')
	if curr_row == height:
		return 1
	if curr_col == width:
		return 1

	num_ways = num_ways_to_traverse_graph(width, height, curr_row+1, curr_col) + \
			   num_ways_to_traverse_graph(width, height, curr_row, curr_col+1)

	return num_ways


import json
test_cases = json.load(open('./test_cases.json'))
itr = 0
for test in test_cases:
	if itr != 0:
		continue
	num_ways = num_ways_to_traverse_graph(test['input']['width'], test['input']['height'])
	print(f'num_ways = {num_ways}')
	if num_ways == test['expected_output']:
		print(f'\tPassed')

	itr += 1

