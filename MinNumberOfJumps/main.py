import sys


def min_number_of_jumps(array):
	n = len(array)
	# memo = [-1] * n
	# return min_number_of_jumps_memoization(array, n, memo)
	return min_number_of_jumps_tabulation(array, n)


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
	jumps = [0 if itr == 0 else sys.maxsize for itr in range(n)]
	for i in range(n):
		for j in range(i+1, i+array[i]+1):
			if j >= n:
				continue
			jumps[j] = min(1 + jumps[i], jumps[j])
	return jumps[n-1]



# print(f'\n\n')
# import json
# test_cases = json.load(open('test_cases.json'))
# for test_case in test_cases:
# 	print(test_case['input'])
# 	output = min_number_of_jumps(test_case['input'])
# 	print(f'\t{output}')
# 	if output == test_case['expected_output']:
# 		print(f'\tPassed')
