
# TODO: add solution
def four_number_sum(array, target_sum):
	print(f'{array} | {target_sum}')

	return []


if __name__ == '__main__':
	print(f'\n\n\n')
	import json
	test_cases = json.load(open('test_cases.json', mode='r'))
	for test_case in test_cases:
		input_params = test_case['input']
		result = four_number_sum(input_params['array'], input_params['targetSum'])
