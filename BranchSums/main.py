from trees import *


# Binary tree Implementation from AlgoExpert
# This implentation does not take into account the relation of the values being inserted into the tree
# so parent: 1; left: 2; right: 3 is possible.
# Even though in an actual BST, the expected tree would be: parent 1; right: 2; right.right: 3
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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


def branch_sums(tree: BinaryTree):
    sums = []
    branch_sum_helper(tree, sums, 0)
    return sums


def branch_sum_helper(root, sums, curr_sum):
    if root is None:
        return

    updated_sum = curr_sum + root.value
    if root.left is None and root.right is None:
        sums.append(updated_sum)
        return

    branch_sum_helper(root.left, sums, updated_sum)
    branch_sum_helper(root.right, sums, updated_sum)


def branch_sums_iterative(tree):

    stack = []
    stack.append(tree)

    sums = []
    sum = 0

    while stack:
        curr_node = stack.pop()
        sum += curr_node.value

        if curr_node.left is None and curr_node.right is None:
            print(f'adding sum: {sum}')
            sums.append(sum)

        if curr_node.right is not None:
            stack.append(curr_node.right)
        if curr_node.left is not None:
            stack.append(curr_node.left)

    print(f'sums: {sums}')


