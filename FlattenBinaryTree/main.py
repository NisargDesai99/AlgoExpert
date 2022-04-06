# This is the class of the input root. Do not edit it.
class BinaryTree:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

		def __repr__(self):
			return str(self.value)

		def __str__(self):
			return str(self.value)


def get_inorder(tree, list_tree):
	if tree is None:
		return []
	get_inorder(tree.left, list_tree)
	list_tree.append(tree)
	get_inorder(tree.right, list_tree)
	return list_tree


# simple solution
def flattenBinaryTree(root):
	inorder_list = get_inorder(root, [])
	for idx in range(len(inorder_list)):
		if idx <= len(inorder_list) - 2:
			inorder_list[idx].right = inorder_list[idx+1]
		if idx >= 1:
			inorder_list[idx].left = inorder_list[idx-1]
	return inorder_list[0]
