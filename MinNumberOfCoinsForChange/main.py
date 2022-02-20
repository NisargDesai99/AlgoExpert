import json


def min_num_coins_change(n, denoms):



	return 0


test_cases = [
	{
		"input": {
			"n": 24,
			"denoms": [1, 5, 10]
		},
		"expected_output": 6
	}
]

# test_cases = json.load(open('./test_cases.json'))
for test in test_cases:
	min_coins = min_num_coins_change(test['input']['n'], test['input']['denoms'])
	print(f'{min_coins}: min_coins')



