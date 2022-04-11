
def spiral_traverse(array):
	spiral = []

	start_row, end_row = 0, len(array) - 1
	start_col, end_col = 0, len(array[0]) - 1

	if end_row == -1:
		return spiral

	while start_row <= end_row and start_col <= end_col:

		for i in range(start_col, end_col + 1):
			spiral.append(array[start_row][i])

		for j in range(start_row + 1, end_row + 1):
			spiral.append(array[j][end_col])

		for i in range(end_col - 1, start_col-1, -1):
			if start_row == end_row:
				break
			spiral.append(array[end_row][i])

		for j in range(end_row-1, start_row, -1):
			if start_col == end_col:
				break
			spiral.append(array[j][start_col])

		start_row += 1
		start_col += 1
		end_row -= 1
		end_col -= 1

	return spiral


