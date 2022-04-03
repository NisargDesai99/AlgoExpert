# This is the class of the input root. Do not edit it.
class BinaryTree:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def insert(self, values, i=0):
		if i >= len(values):
			return
		queue = [self]
		while len(queue) > 0:
			current = queue.pop(0)
			if current.left is None:
				current.left = BinaryTree(values[i])
				break
			queue.append(current.left)
			if current.right is None:
				current.right = BinaryTree(values[i])
				break
			queue.append(current.right)
		self.insert(values, i + 1)
		return self

	# def leftToRightToLeft(self):
	# 	nodes = []
	# 	current = self
	# 	while current.right is not None:
	# 		nodes.append(current.value)
	# 		current = current.right
	# 	nodes.append(current.value)
	# 	while current is not None:
	# 		nodes.append(current.value)
	# 		current = current.left
	# 	return nodes


# space optimized solution
def flatten_binary_tree(root):
	left, right = flatten_binary_tree_helper(root)
	return left


def flatten_binary_tree_helper(root):
	if root.left is None:
		left_most = root
	else:
		left_subtree_left_most, left_subtree_right_most = \
			flatten_binary_tree_helper(root.left)
		connect_nodes(left_subtree_right_most, root)
		left_most = left_subtree_left_most

	if root.right is None:
		right_most = root
	else:
		right_subtree_left_most, right_subtree_right_most = \
			flatten_binary_tree_helper(root.right)
		connect_nodes(root, right_subtree_left_most)
		right_most = right_subtree_right_most

	return [left_most, right_most]


def connect_nodes(left, right):
	left.right = right
	right.left = left


# from collections import deque
# def create_tree(tree):
# 	root = tree['root']
# 	root_node = BinaryTree(int(tree['root']))
# 	tree_nodes = {int(tree['root']): root_node}

# 	for node in tree['nodes']:
# 		if node['value'] in tree_nodes:
# 			if node['left'] is not None:
# 				left_node = BinaryTree('')



# import json
# test_cases = json.load(open('test_cases.json', mode='r'))
# for test_case in test_cases:
# 	create_tree(test_case['input']['tree'])

