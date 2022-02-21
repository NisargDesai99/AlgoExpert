import sys


def min_num_coins_change_recursive(n, denoms):
	if n == 0:
		return 0

	min_count = sys.maxsize

	for i in range(len(denoms)):
		if denoms[i] > n:
			continue

		curr_count = min_num_coins_change_recursive(n - denoms[i], denoms)
		if curr_count != sys.maxsize and curr_count + 1 < min_count:
			min_count = curr_count + 1

	return -1 if min_count == sys.maxsize else min_count


def min_num_coins_change_memoization(n, denoms):
	if n == 0:
		return 0

	table = [sys.maxsize] * (n+1)
	table[0] = 0

	for i in range(1, n+1):
		for denom in denoms:
			if denom > i:
				continue

			curr_count = table[i-denom] + 1
			if curr_count != sys.maxsize and curr_count < table[i]:
				table[i] = curr_count

	return -1 if table[n] == sys.maxsize else table[n]

# import json
# test_cases = json.load(open('./test_cases.json'))
# for test in test_cases:
# 	min_coins = min_num_coins_change_memoization(test['input']['n'], test['input']['denoms'])
# 	print(f'min_coins = {min_coins}')
# 	if min_coins == test['expected_output']:
# 		print(f'\tPassed')
