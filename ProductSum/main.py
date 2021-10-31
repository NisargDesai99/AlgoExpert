# TODO: Product Sum
# https://www.algoexpert.io/questions/Product%20Sum


def productSum(array):
	# return product_sum_helper(array, 0, 0, 1)
	return product_sum_helper_cleaned_up(array, 1)


def product_sum_helper(array, index, curr_sum, level):
	
	print(f'array = {array}; '
		  f'curr item = {array[index]}; '
		  f'curr_sum = {curr_sum}; '
		  f'level = {level}')

	length = len(array)
	while (index < length):
		if type(array[index]) is int:
			curr_sum += array[index]
			index += 1
			print(f'index = {index}')
		elif type(array[index]) is list:
			print(f'recursing with index = {index}')
			curr_sum += product_sum_helper(array[index], 0, 0, level + 1)
			index += 1
		
		if index == length:
			return level * curr_sum

	return curr_sum


def product_sum_helper_cleaned_up(array, level):
	curr_sum = 0
	for item in array:
		if type(item) is list:
			curr_sum += product_sum_helper_cleaned_up(item, level + 1)
		else:
			curr_sum += item
	return level * curr_sum


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(productSum(array))


