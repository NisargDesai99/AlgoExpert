# This is the class of the input root. Do not edit it.
class BinaryTree:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


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
