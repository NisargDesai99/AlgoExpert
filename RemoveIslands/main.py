from collections import deque


def is_coordinate_valid(row, col, width, height):
	return (height > row >= 0) and (width > col >= 0)


def is_border(row, col, width, height):
	return (row == 0 or row == height - 1) or (col == 0 or col == width - 1)


def get_neighbors(matrix, row, col):
	neighbors = []
	num_rows = len(matrix)
	num_cols = len(matrix[0])

	if row - 1 >= 0:
		neighbors.append((row - 1, col))
	if row + 1 < num_rows:
		neighbors.append((row + 1, col))
	if col - 1 >= 0:
		neighbors.append((row, col - 1))
	if col + 1 < num_cols:
		neighbors.append((row, col + 1))

	return neighbors


def update_connected_ones(curr_row, curr_col, matrix):
	stack = deque()
	stack.append((curr_row, curr_col))

	while stack:
		row, col = stack.pop()
		matrix[row][col] = 2

		neighbors = get_neighbors(matrix, row, col)

		for neighbor in neighbors:
			n_row, n_col = neighbor

			if matrix[n_row][n_col] != 1:
				continue

			stack.append(neighbor)


def remove_islands(matrix):

	row = 0
	col = 0

	width = len(matrix[0])
	height = len(matrix)

	for curr_row in range(height):
		for curr_col in range(width):
			if not is_border(curr_row, curr_col, width, height):
				continue
			if matrix[curr_row][curr_col] != 1:
				continue

			update_connected_ones(curr_row, curr_col, matrix)

	for curr_row in range(height):
		for curr_col in range(width):
			if matrix[curr_row][curr_col] == 1:
				matrix[curr_row][curr_col] = 0
			if matrix[curr_row][curr_col] == 2:
				matrix[curr_row][curr_col] = 1

	return matrix


matrix = [
	[1, 0, 0, 0, 0, 0],
	[0, 1, 0, 1, 1, 1],
	[0, 0, 1, 0, 1, 0],
	[1, 1, 0, 0, 1, 0],
	[1, 0, 1, 1, 0, 0],
	[1, 0, 0, 0, 0, 1],
]

# matrix = [
# 	[1, 0, 0, 1, 0],
#     [0, 1, 0, 1, 0],
#     [0, 0, 1, 1, 0]
# ]


print('input')
print(''.join([str(row) + '\n' for row in matrix]))
result = remove_islands(matrix)
print('result')
print(''.join([str(row) + '\n' for row in result]))

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

