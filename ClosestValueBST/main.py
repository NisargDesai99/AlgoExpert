from trees import *

def closest_value_bst(tree: BST, target):
	tree.show()
	current_node = tree.root
	closest_value = tree.root.value
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

