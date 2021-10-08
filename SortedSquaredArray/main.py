def sorted_squared_array(array):
	left = 0
	right = len(array) - 1
	squared_arr = [0] * len(array)

	counter = len(array) - 1
	while counter >= 0:
		if abs(array[left]) > abs(array[right]):
			squared_arr[counter] = array[left] * array[left]
			left += 1
		else:
			squared_arr[counter] = array[right] * array[right]
			right -= 1
		counter -= 1
	
	return squared_arr

