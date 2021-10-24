# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class AlgoExpertBST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	
	def __repr__(self):
		return str(self.value)

	def __str__(self):
		return str(self.value)

	def insert(self, value):
		curr_node = self
		parent = None
		while curr_node is not None:
			parent = curr_node
			if value < curr_node.value:
				curr_node = curr_node.left
			elif value >= curr_node.value:
				curr_node = curr_node.right
		if value < parent.value:
			parent.left = AlgoExpertBST(value)
		elif value >= parent.value:
			parent.right = AlgoExpertBST(value)
		else:
			parent = AlgoExpertBST(value)
		return self

	def contains(self, value):
		curr_node = self
		while curr_node is not None:
			if value < curr_node.value:
				curr_node = curr_node.left
			elif value > curr_node.value:
				curr_node = curr_node.right
			elif value == curr_node.value:
				return True
		return False
			

	def remove(self, value):
		curr_node = self
		parent = None
		is_left_child = False

		while curr_node.value != value and curr_node is not None:
			parent = curr_node
			if value < curr_node.value:
				is_left_child = True
				curr_node = curr_node.left
			elif value > curr_node.value:
				is_left_child = False
				curr_node = curr_node.right

		if curr_node is None:
			print(f'Value to remove not found')
			return

		has_left = curr_node.left is not None
		has_right = curr_node.right is not None
		
		if has_left and has_right:
			replacement_parent, replacement_node = self.__get_inorder_successor(curr_node)
			if replacement_parent is not None:
				replacement_parent.left = replacement_node.right
			else:
				curr_node.right = replacement_node.right
			curr_node.value = replacement_node.value
			curr_node = None
		elif has_right or has_left:
			replacement_node = curr_node.left if has_left else curr_node.right
			if parent is None:
				curr_node.value = replacement_node.value
				curr_node.left = replacement_node.left
				curr_node.right = replacement_node.right
				return
			if is_left_child:
				parent.left = replacement_node
			else:
				parent.right = replacement_node
		else:
			if parent is None:
				return
			if is_left_child:
				parent.left = None
			else:
				parent.right = None
		return

	def __get_inorder_successor(self, node):
		parent = None
		iterator_node = node.right
		while iterator_node.left is not None:
			parent = iterator_node
			iterator_node = iterator_node.left
		return (parent, iterator_node)

	def show(self):
		if self.value is None and self.left is None and self.right is None:
			print('Tree is empty...')
			return
		print(', '.join(BST.__get_as_preorder_list(self)))

	@staticmethod
	def __get_as_preorder_list(curr_node):
		tree_stack = [curr_node]
		preorder_list = []
		while len(tree_stack) != 0:
			curr_node = tree_stack.pop()
			preorder_list.append(str(curr_node))
			if curr_node.right is not None:
				tree_stack.append(curr_node.right)
			if curr_node.left is not None:
				tree_stack.append(curr_node.left)
		return preorder_list