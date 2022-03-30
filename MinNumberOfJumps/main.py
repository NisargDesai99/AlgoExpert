import sys


def min_number_of_jumps(array):
	memo = [-1] * len(array)
	return min_number_of_jumps_memoization(array, len(array), memo)


def min_number_of_jumps_recursive(array, n, idx=0):
	if idx == n-1:
		return 0

	jumps = []
	for i in range(idx+1, idx+array[idx]+1):
		if i <= n-1:
			jumps.append(1 + min_number_of_jumps_recursive(array, n, i))

	min_jumps = min(jumps)
	return min_jumps


def min_number_of_jumps_memoization(array, n, memo, idx=0):
	if idx < n and memo[idx] != -1:
		return memo[idx]
	if idx == n-1:
		return 0

	min_jumps = sys.maxsize
	for i in range(idx+1, idx+array[idx]+1):
		if i >= n:
			continue
		jumps = 1 + min_number_of_jumps_memoization(array, n, memo, i)
		if jumps < min_jumps:
			min_jumps = jumps

	memo[idx] = min_jumps
	return memo[idx]


def min_number_of_jumps_tabulation(array, n):
	jumps = []



print(f'\n\n')
import json
test_cases = json.load(open('test_cases.json'))
counter = 0
for test_case in test_cases:
	if counter != 0:
		continue

	print(test_case['input'])
	output = min_number_of_jumps(test_case['input'])
	print(f'\t{output}')
	if output == test_case['expected_output']:
		print(f'\tPassed')

	counter += 1
