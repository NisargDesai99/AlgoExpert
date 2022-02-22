

def num_ways_to_traverse_graph(width, height, curr_row=1, curr_col=1):
	# print(f'{curr_row}: {height}')
	# print(f'{curr_col}: {width}')
	if curr_row == height:
		return 1
	if curr_col == width:
		return 1

	num_ways = num_ways_to_traverse_graph(width, height, curr_row+1, curr_col) + \
			   num_ways_to_traverse_graph(width, height, curr_row, curr_col+1)

	return num_ways


def temp(width, height):
	if width == 1 or height == 1:
		return 1

	return temp(width-1, height) + temp(width, height-1)


import json
test_cases = json.load(open('./test_cases.json'))
itr = 0
for test in test_cases:
	if itr != 0:
		continue
	num_ways = num_ways_to_traverse_graph(test['input']['width'], test['input']['height'])
	print(f'input: {test["input"]}')
	print(f'num_ways = {num_ways}')
	if num_ways == test['expected_output']:
		print(f'\tPassed')

	itr += 1

