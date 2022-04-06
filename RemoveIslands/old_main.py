from collections import deque


def remove_islands_old(matrix):
	result = []
	stack = deque()
	stack.append((0,0))

	border_1s = set()
	
	row_len = len(matrix[0])
	col_len = len(matrix)

	while stack:
		row, col = stack.pop()
		print(f'popped val: ({row}, {col})')

		if (row == 0 or col == 0) and matrix[row][col] == 1:
			border_1s.add((row, col))

		print(f'border_1s = {border_1s}')

		if row+1 < row_len and matrix[row+1][col] == 1:
			stack.append((row+1, col))
		if col+1 < col_len and matrix[row][col+1] == 1:
			stack.append((row, col+1))

		temp_col = col + 1
		while temp_col < col_len:
			# matrix[row][temp_col] != 1
			# if matrix[row][temp_col] == 1:
			# 	border_1s.add((row, temp_col))
			stack.append((row, temp_col))
			temp_col += 1

		temp_row = row + 1
		while temp_row < row_len:
			# matrix[temp_row][col] != 1
			stack.append((temp_row, col))
			temp_row += 1


	# for row in range(row_len):
	# 	for col in range(col_len):
	# 		print(f'({row}, {col}): {matrix[row][col]}')

	return result


def is_border(coordinates, horiz_len, vert_len):
	row, col = coordinates
	if row == 0 or row == horiz_len - 1 or col == 0 or col == vert_len - 1:
		return True


def remove_islands(matrix):

	stack = deque()
	stack.append((0,0))

	# dimensions = (num rows x num cols)
	dimensions = (len(matrix[0]), len(matrix))

	island_indices = set()

	row = 0
	col = 0

	while stack:
		curr_row, curr_col = stack.pop()
		if curr_row >= 1:
			print(curr_row)

		if matrix[curr_row][curr_col] == 1 and is_border((curr_row, curr_col), horiz_len=6, vert_len=6):
			island_indices.add((curr_col, curr_row))

		stack.append((curr_row + 1, curr_col))
		stack.append((curr_row, curr_col + 1))


matrix = [
	[1, 0, 0, 0, 0, 0],
	[0, 1, 0, 1, 1, 1],
	[0, 0, 1, 0, 1, 0],
	[1, 1, 0, 0, 1, 0],
	[1, 0, 1, 1, 0, 0],
	[1, 0, 0, 0, 0, 1]
]

remove_islands(matrix)

"""
given:
	2D Array of potentially UNEQUAL HEIGHT AND WIDTH
	contains 0s and 1s
	0 - white
	1 - black

Island:
	1s that are horizontally or vertically adjacent (but not diagonally)
	1s that don't touch border of the image
	Group is not an island if any 1s are in first/last row or first/last col

	1 0 0 0 0 0
	0 1 0 1 1 1
	0 0 1 0 1 0
	1 1 0 0 1 0
	1 0 1 1 0 0
	1 0 0 0 0 1

	add borders to stack
	iterate over border stack
		find islands

"""
