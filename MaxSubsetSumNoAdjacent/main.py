

def max_subset_sum_no_adjacent(array):
	
	max_sum = -1
	curr_sum = 0

	for i in range(0, len(array), 2):
		i+=1
		print(f'array[{i}] = {array[i]}')
		if i == 0:
			curr_sum = array[i]
			print(f'idx 0 - curr_sum = {curr_sum}')
			continue

		if i+1 < len(array) and array[i] < array[i+1]:
			print(f'next num larger... continuing')
			continue

		curr_sum += array[i]
		print(f'adding {array[i]} - new curr_sum = {curr_sum}')

	return curr_sum
		



arr = [75, 105, 120, 75, 90, 135]
print(f'input: {arr}')
print(f'result: {max_subset_sum_no_adjacent(arr)}', end='\n\n')

arr2 = [135, 90, 75, 120, 105, 75]
print(f'input: {arr2}')
print(f'result: {max_subset_sum_no_adjacent(arr2)}', end='\n\n')

