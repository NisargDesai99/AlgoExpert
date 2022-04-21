
def zigzag_traverse(array):

	row, end_row = 0, len(array)
	col, end_col = 0, len(array[0])

	zigzag = []
	up_right = False

	while 0 <= row < end_row and 0 <= col < end_col:
		zigzag.append(array[row][col])

		if up_right:
			if row == 0 or col == end_col - 1:
				up_right = False
				if col == end_col - 1:
					row += 1
				else:
					col += 1
			else:
				row -= 1
				col += 1
		else:
			if col == 0 or row == end_row - 1:
				up_right = True
				if row == end_row - 1:
					col += 1
				else:
					row += 1
			else:
				row += 1
				col -= 1

	return zigzag

# if row == 0 or col == 0 or row == end_row or col == end_col:
# 	if up_right and col + 1 < end_col:
# 		col += 1
# 	elif up_right and col >= end_col:
# 		row += 1
# 		up_right = False
# 	elif not up_right and row < end_row:
# 		row += 1
# 		up_right = True
# 	elif not up_right and row >= end_row:
# 		col += 1
# 	row_increment = row_increment * -1
# 	col_increment = col_increment * -1
# 	continue


if __name__ == '__main__':
	import json

	test_cases = [json.load(open('test_cases.json', mode='r'))[0]]
	for test_case in test_cases:
		result = zigzag_traverse(test_case['input'])
		print(result)

