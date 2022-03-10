
def merge_sort(arr):
	half = int((len(arr)-1)/2)
	merge_sort_helper(arr[:half+1], arr[half+1:])


def merge_sort_helper(arr1, arr2):
	print(arr1, '|', arr2)

	# base case
	if len(arr1) == 1 and len(arr2) == 1:
		if arr1[0] > arr2[0]:
			return [arr2[0], arr1[0]]
		else:
			return [arr1[0], arr2[0]]

	# get lengths and half lengths
	arr1_len, arr2_len = len(arr1), len(arr2)
	half_arr1, half_arr2 = int((arr1_len-1)/2), int((arr2_len-1)/2)

	# recursive call
	sorted_arr1 = merge_sort_helper(arr1[:half_arr1+1], arr1[half_arr1+1:])
	sorted_arr2 = merge_sort_helper(arr2[:half_arr2+1], arr2[half_arr2+1:])

	# combine sorted arrays
	ctr_arr1, ctr_arr2 = 0, 0
	new_arr = []
	for i in range(len(sorted_arr1) if len(sorted_arr1) > len(sorted_arr2) else len(sorted_arr2)):
		# both have a value
		if sorted_arr1[ctr_arr1] >= sorted_arr2[ctr_arr2]:
			new_arr.append(sorted_arr2[ctr_arr2])
			new_arr.append(sorted_arr1[ctr_arr1])
			ctr_arr1 += 1
			ctr_arr2 += 1
		elif sorted_arr1[ctr_arr1] < sorted_arr2[ctr_arr2]:
			new_arr.append(sorted_arr1[ctr_arr1])
			new_arr.append(sorted_arr2[ctr_arr2])
			ctr_arr1 += 1
			ctr_arr2 += 1
		# one array shorter than other
		else:
			if ctr_arr1 < len(sorted_arr1):
				new_arr.append(sorted_arr1[ctr_arr1])
				ctr_arr1 += 1
			if ctr_arr2 < len(sorted_arr2):
				new_arr.append(sorted_arr2[ctr_arr2])
				ctr_arr2 += 1

	print(f'combined: {new_arr}')
	# return combined array
	return new_arr


import json
test_cases = json.load(open('./test_cases.json', mode='r'))
for test in test_cases:
	merge_sort(test['input'])
