

def move_element_to_end(array, toMove):
	i = 0
	j = len(array) - 1
	while i < j:
		while i < j and array[j] == toMove:
			j -= 1
		if array[i] == toMove:
			temp = array[j]
			array[j] = array[i]
			array[i] = temp
		i += 1

	return array


