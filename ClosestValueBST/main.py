
def print_tree(tree):
	print(f'{tree.value}', end=' ')
	if tree.left is not None:
		print_tree(tree.left)
	if tree.right is not None:
		print_tree(tree.right)


def closest_value_bst(tree, target):
	print_tree(tree)
	current_node = tree
	closest_value = tree.value
	while current_node is not None:
		if abs(target - current_node.value) < abs(target - closest_value):
			closest_value = current_node.value
		
		if target < current_node.value:
			current_node = current_node.left
		elif target > current_node.value:
			current_node = current_node.right
		else:
			break
	
	return closest_value


class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


