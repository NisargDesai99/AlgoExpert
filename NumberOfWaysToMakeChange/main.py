def number_of_ways_to_make_change(n, denoms, curr_ways=0):
	if n < 0:
		return 0
	if n == 0:
		return 1
	if len(denoms) == 0 and n != 0:
		return 0

	return number_of_ways_to_make_change(n, denoms[0:-1], curr_ways) + \
		number_of_ways_to_make_change(n - denoms[-1], denoms, curr_ways)


def num_ways_memoization(n, denoms):
	ways = [0 for i in range(n+1)]
	ways[0] = 1
	for denom in denoms:
		for amount in range(1, n+1):
			if denom > amount:
				continue
			ways[amount] += ways[amount - denom]
	return ways[-1]

# import json
# test_cases = json.load(open('./test_cases.json'))
# for test in test_cases:
# 	min_coins = num_ways_memoization(test['input']['n'], test['input']['denoms'])
# 	print(f'min_coins = {min_coins}')
# 	if min_coins == test['expected_output']:
# 		print(f'\tPassed')
