

# from BSTConstruction.main import AlgoExpertBST
from trees import BST
from trees.bst import Node, TraversalMode


def validate_vst(tree: BST):
	validate_tree_helper(tree)


def validate_tree_helper(tree):
	iter_stack = [{"node": tree.root, "type": "root"}]
	parent = None

	while len(iter_stack) > 0:
		item = iter_stack.pop()
		curr_node, type = item["node"], item["type"]
		has_parent = parent is not None

		if has_parent and type == "root":
			print("Tree only has a root. Valid.")
			return True

		if type == "left" and curr_node >= parent:
			return False
		if type == "right" and curr_node < parent:
			return False

		if curr_node.right is not None:
			iter_stack.append({"node": curr_node.right, "type": "right"})
		if curr_node.left is not None:
			iter_stack.append({"node": curr_node.left, "type": "left"})

		parent = curr_node

	return True


bst = BST()

for item in [10, 5, 15, 2, 3, 6, 4, 17, 18]:
	bst.insert(item, traversal_mode=TraversalMode.ITERATIVE)

# bst.root.right.left = Node(16)

print(f'validate: {validate_tree_helper(bst)}')

