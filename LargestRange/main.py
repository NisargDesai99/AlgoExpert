import json
import sys


def largest_range(array):
	res_range = []
	nums_dict = {key: False for key in array}
	max_length = -1

	for curr_num in array:
		if nums_dict[curr_num]:
			continue

		left = curr_num - 1
		right = curr_num + 1
		curr_length = 1

		while left in nums_dict:
			nums_dict[left] = True
			left -= 1
			curr_length += 1

		while right in nums_dict:
			nums_dict[right] = True
			right += 1
			curr_length += 1

		if curr_length > max_length:
			max_length = curr_length
			res_range = [left+1, right-1]

	return res_range


# optimized to O(n) time using O(n) space
def largest_range_dirty_code(array):
	nums_dict = {key: False for key in array}

	max_left = sys.maxsize
	max_right = -sys.maxsize - 1
	for curr_num in array:
		if nums_dict[curr_num]:
			continue
		left_most = curr_num
		right_most = curr_num
		nums_dict[curr_num] = True
		for j in range(curr_num-1, -sys.maxsize-1, -1):
			if j in nums_dict and j < left_most:
				left_most = j
				nums_dict[j] = True
			else:
				break

		for k in range(curr_num+1, sys.maxsize):
			if k in nums_dict and k > right_most:
				right_most = k
				nums_dict[k] = True
			else:
				break

		if right_most - left_most > max_right - max_left:
			max_left = left_most
			max_right = right_most

	return [max_left, max_right]


# O(nlog(n)) time bc of sort | O(1) space
def largest_range_sorted(array):
	if array is None:
		array = []

	if len(array) == 1:
		return [array[0], array[0]]

	array.sort()

	max_range = -1
	max_num1_idx = 0
	max_num2_idx = 0
	num1_idx = 0
	num2_idx = 1
	for i in range(1, len(array)):
		if array[i-1] + 1 == array[i]:
			num2_idx += 1
		else:
			if num2_idx - num1_idx > max_range:
				max_range = num2_idx - num1_idx
				max_num1_idx = num1_idx
				max_num2_idx = num2_idx - 1
			num1_idx = i
			continue

		if num2_idx - num1_idx > max_range:
			max_range = num2_idx - num1_idx
			max_num1_idx = num1_idx
			max_num2_idx = num2_idx - 1

	return [array[max_num1_idx], array[max_num2_idx]]


if __name__ == '__main__':
	import time
	print(f'\n\n\n')
	test_cases = json.load(open('test_cases.json', mode='r'))
	start_time = time.time()
	for test_case in test_cases:
		result = largest_range(test_case['input'])
	end_time = time.time()
	print(f'clean code time: {end_time - start_time}')

	start_time = time.time()
	for test_case in test_cases:
		result = largest_range_dirty_code(test_case['input'])
	end_time = time.time()
	print(f'dirty code time: {end_time - start_time}')

	start_time = time.time()
	for test_case in test_cases:
		result = largest_range_sorted(test_case['input'])
	end_time = time.time()
	print(f'sort array time: {end_time - start_time}')
