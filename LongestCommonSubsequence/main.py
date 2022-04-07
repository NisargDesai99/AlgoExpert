

# TODO: DYNAMIC PROGRAMMING - longest common subsequence
def longest_common_subsequence(str1, str2):
	s1_len = len(str1)
	s2_len = len(str2)

	# solution = longest_common_subsequence_recursive(str1, str2, s1_len, s2_len)

	# memo = [[None for s2 in str2] for s1 in str1]
	# memo = [["" if i == 0 or j == 0 else None for j in range(s1_len+1)] for i in range(s1_len+1)]
	# solution = longest_common_subsequence_memoization(str1, str2, s1_len, s2_len, memo)

	# solution = longest_common_subsequence_tabulation(str1, str2)
	solution = longest_common_subsequence_tabulation_optimized_space(str1, str2)

	return solution


def longest_common_subsequence_recursive_count(str1, str2, s1_len, s2_len):
	if s1_len <= 0 or s2_len <= 0:
		return 0

	if str1[s1_len-1] == str2[s2_len-1]:
		return 1 + longest_common_subsequence_recursive_count(str1, str2, s1_len-1, s2_len-1)
	else:
		return max(longest_common_subsequence_recursive_count(str1, str2, s1_len-1, s2_len),
				   longest_common_subsequence_recursive_count(str1, str2, s1_len, s2_len-1))


# NOTE: this solution uses string appends which cost O(len(s1) + len(s2))
def longest_common_subsequence_recursive(str1, str2, s1_len, s2_len):
	if s1_len <= 0 or s2_len <= 0:
		return ""

	if str1[s1_len-1] == str2[s2_len-1]:
		return longest_common_subsequence_recursive(str1, str2, s1_len-1, s2_len-1) + str1[s1_len-1]
	else:
		left = longest_common_subsequence_recursive(str1, str2, s1_len-1, s2_len)
		up = longest_common_subsequence_recursive(str1, str2, s1_len, s2_len-1)
		return left if len(left) > len(up) else up


# NOTE: this solution uses string appends which cost O(len(s1) + len(s2))
def longest_common_subsequence_memoization(str1, str2, s1_len, s2_len, memo):
	if s1_len == 0 or s2_len == 0:
		return ""

	if memo[s1_len][s2_len] is not None:
		return memo[s1_len][s2_len]

	if str1[s1_len-1] == str2[s2_len-1]:
		memo[s1_len][s2_len] = longest_common_subsequence_memoization(str1, str2, s1_len-1, s2_len-1, memo) + str1[s1_len-1]
		return memo[s1_len][s2_len]
	else:
		left = longest_common_subsequence_memoization(str1, str2, s1_len-1, s2_len, memo)
		up = longest_common_subsequence_memoization(str1, str2, s1_len, s2_len-1, memo)
		memo[s1_len][s2_len] = left if len(left) > len(up) else up
		return memo[s1_len][s2_len]


# NOTE: this solution uses string appends which cost O(len(s1) + len(s2))
# Time = Space = O(nm * min(n,m)) - nm sized table with storing strings of size min(n,m) at each index in the table
def longest_common_subsequence_tabulation(str1, str2):
	s1_len = len(str1)
	s2_len = len(str2)

	lcs_table = [["" if i == 0 or j == 0 else None for j in range(s2_len+1)] for i in range(s1_len+1)]

	for i in range(1, s1_len+1):
		for j in range(1, s2_len+1):
			if str1[i-1] == str2[j-1]:
				lcs_table[i][j] = lcs_table[i-1][j-1] + str1[i-1]
			else:
				lcs_table[i][j] = max(lcs_table[i-1][j], lcs_table[i][j-1], key=len)

	return lcs_table[s1_len][s2_len]


# Time = O(nm) | Space = O(nm)
def longest_common_subsequence_tabulation_optimized_space(str1, str2):
	s1_len = len(str1)
	s2_len = len(str2)

	lcs_table = [[{'char': None, 'len': 0, 'prev_char': (None, None)} if i == 0 or j == 0 else None for j in range(s2_len+1)] for i in range(s1_len+1)]

	for i in range(1, s1_len+1):
		for j in range(1, s2_len+1):
			if str1[i-1] == str2[j-1]:
				lcs_table[i][j] = {'char': str1[i-1], 'len': lcs_table[i-1][j-1]['len']+1, 'prev_char': (i-1, j-1)}
			else:
				up = lcs_table[i-1][j]
				left = lcs_table[i][j-1]
				if up['len'] > left['len']:
					lcs_table[i][j] = {'char': None, 'len': up['len'], 'prev_char': (i-1, j)}
				else:
					lcs_table[i][j] = {'char': None, 'len': left['len'], 'prev_char': (i, j-1)}

	def build_subsequence(table):
		sequence = []
		row = len(table) - 1
		col = len(table[0]) - 1

		while row > 0 and col > 0:
			curr = table[row][col]
			if curr['char'] is not None:
				sequence.append(curr['char'])
			row, col = curr['prev_char']

		return list(reversed(sequence))

	return build_subsequence(lcs_table)


if __name__ == '__main__':
	import json
	test_cases = json.load(open('./test_cases.json', mode='r'))
	for test_case in test_cases:
		input_strs = test_case['input']
		# print(f'--------------------')
		result = longest_common_subsequence(input_strs['str1'], input_strs['str2'])
		print(f"inputs: \"{input_strs['str1']}\", \"{input_strs['str2']}\" || result: {result}")
		# print(f'--------------------')
		# print(f'result: {"".join([item for item in result])}')

