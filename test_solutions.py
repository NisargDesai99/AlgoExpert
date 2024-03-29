
import os
import json
import unittest
import global_vars
# from trees import BinarySearchTree


class Colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	WHITE = '\033[37m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


class TestSolutions(unittest.TestCase):

	@staticmethod
	def read_test_cases(problem_dir):
		print(f'Reading test cases for {problem_dir}')
		path = f'{global_vars.PROJECT_PATH}/{problem_dir}/test_cases.json'
		test_cases_file = open(path)
		test_cases = json.load(test_cases_file)
		test_cases_file.close()
		return test_cases

	@staticmethod
	def display(test_case, result):
		print(f'Inputs: {test_case["input"]};\n\t'
			  f'{Colors.OKCYAN}Expected Output: {test_case["expected_output"]}\n\t'
			  f'{Colors.OKCYAN}Result: {result};\n\t'
			  f'{f"{Colors.OKGREEN}Passed{Colors.WHITE}" if test_case["expected_output"] == result else f"{Colors.FAIL}Failed"}{Colors.WHITE}')

	def test_non_constructible_change(self):
		print('\n-----Non-ConstructibleChange-----')
		from NonConstructibleChange import main

		test_cases = TestSolutions.read_test_cases('NonConstructibleChange')

		all_cases_passed = True
		counter = 1
		for test_case in test_cases:
			result = main.non_constructible_change(test_case['input'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
			counter += 1

		print('-----Non-ConstructibleChange-----\n')
		assert all_cases_passed

	def test_validate_subsequence(self):
		# print('\n-----Validate Subsequence-----')
		# from ValidateSubsequence import main

		# test_cases = TestSolutions.TestSolutions.read_test_cases('ValidateSubsequence')

		# all_cases_passed = True
		# for test_case in test_cases:
		# 	is_subsequence = main.validate_subsequence(test_case['array'], test_case['sequence'])
		# 	print(f'arr: {test_case["array"]}; seq: {test_case["sequence"]};\n\t'
		# 		  f'Result: {is_subsequence}; '
		# 		  f'{"Passed" if test_case["expected_output"] == is_subsequence else "Failed"}')
		# 	all_cases_passed = all_cases_passed and (test_case['expected_output'] == is_subsequence)

		# print('-----Validate Subsequence-----\n')
		# assert all_cases_passed
		pass

	def test_sorted_squared_array(self):
		print('\n-----Sorted Squared Array-----')
		from SortedSquaredArray import main

		test_cases = TestSolutions.read_test_cases('SortedSquaredArray')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.sorted_squared_array(test_case['input'])

			all_cases_passed = all_cases_passed and (test_case['expected_output'] == result)
			TestSolutions.display(test_case, result)
		print('-----Sorted Squared Array-----\n')
		assert all_cases_passed

	def test_tournament_winner(self):
		print('\n-----Tournament Winner-----')
		from TournamentWinner import main

		test_cases = TestSolutions.read_test_cases('TournamentWinner')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.tournament_winner(test_case['input']['competitions'], test_case['input']['results'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Tournament Winner-----\n')
		assert all_cases_passed

	def test_closest_value_bst(self):
		# print('\n-----Closest Value BST-----')
		# from ClosestValueBST import main
		# test_cases = TestSolutions.TestSolutions.read_test_cases('ClosestValueBST')
		# # TEST CASES BST INPUTS IN PRE-ORDER
		# # TODO: create BST with pre-order traversal

		# all_cases_passed = True
		# for test_case in test_cases:
		# 	bst = BinarySearchTree()
		# 	bst.build_from_list(test_case['input'])
		# 	target = test_case['target']

		# 	result = main.closest_value_bst(bst, target)

		# 	all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
		# 	print(f'Inputs: {test_case["input"]}; Expected Output: {test_case["expected_output"]}\n\t'
		# 		  f'Result: {result}; {"Passed" if test_case["expected_output"] == result else "Failed"}')

		# print('-----Closest Value BST-----\n')
		# assert all_cases_passed
		pass


	# TODO: finish tests
	def test_branch_sum(self):
		# print('\n-----Branch Sums-----')
		# from BranchSums import main
		# test_cases = TestSolutions.TestSolutions.read_test_cases('BranchSums')

		# for test_case in test_cases:
		# 	continue

		# print('-----Branch Sums-----\n')
		pass


	# TODO: finish tests for BST
	# def test_bst_insert()
	# def test_bst_remove()
	# def test_bst_contains()

	def test_validate_bst(self):
		# print(f'\n-----Validate BST-----')
		# from ValidateBST import main
		# test_cases = TestSolutions.TestSolutions.read_test_cases('ValidateBST')

		# for test_case in test_cases:
		# 	continue

		# print('-----Validate BST-----\n')
		pass

	def test_remove_islands(self):
		print(f'\n-----Remove Islands-----')
		from RemoveIslands import main
		test_cases = TestSolutions.read_test_cases('RemoveIslands')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.remove_islands(test_case['input'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Remove Islands-----\n')
		assert all_cases_passed

	def test_reverse_words_in_string(self):
		print(f'\n-----Reverse Words In String-----')
		from ReverseWordsInString import main
		test_cases = TestSolutions.read_test_cases('ReverseWordsInString')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.reverse_words_in_string(test_case['input'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Reverse Words In String-----\n')
		assert all_cases_passed

	def test_max_subset_sum_no_adjacent(self):
		print(f'\n-----Max Subset Sum No Adjacent-----')
		from MaxSubsetSumNoAdjacent import main
		test_cases = TestSolutions.read_test_cases('MaxSubsetSumNoAdjacent')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.max_subset_sum_no_adjacent(test_case['input'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Max Subset Sum No Adjacent-----\n')
		assert all_cases_passed

	def test_number_of_ways_to_make_change(self):
		print(f'\n-----Number Of Ways To Make Change-----')
		from NumberOfWaysToMakeChange import main
		test_cases = TestSolutions.read_test_cases('NumberOfWaysToMakeChange')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.num_ways_memoization(test_case['input']['n'], test_case['input']['denoms'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Number Of Ways To Make Change-----\n')
		assert all_cases_passed

	def test_min_num_coins_for_change(self):
		print(f'\n-----Min Number Of Coins For Change-----')
		from MinNumberOfCoinsForChange import main
		test_cases = TestSolutions.read_test_cases('MinNumberOfCoinsForChange')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.min_num_coins_change_memoization(test_case['input']['n'], test_case['input']['denoms'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Min Number Of Coins For Change-----\n')
		assert all_cases_passed

	def test_num_ways_to_traverse_graph(self):
		print(f'\n-----Number Of Ways To Traverse Graph-----')
		from NumberOfWaysToTraverseGraph import main
		test_cases = TestSolutions.read_test_cases('NumberOfWaysToTraverseGraph')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.num_ways_to_traverse_graph(test_case['input']['width'], test_case['input']['height'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Number Of Ways To Traverse Graph-----\n')
		assert all_cases_passed

	def test_knapsack_problem(self):
		print(f'\n-----Knapsack Problem-----')
		from KnapsackProblem import main
		test_cases = TestSolutions.read_test_cases('KnapsackProblem')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.knapsack_problem(test_case['input']['items'], test_case['input']['capacity'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Knapsack Problem-----\n')
		assert all_cases_passed

	def test_min_number_of_jumps(self):
		print(f'\n-----Min Number Of Jumps-----')
		from MinNumberOfJumps import main
		test_cases = TestSolutions.read_test_cases('MinNumberOfJumps')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.min_number_of_jumps(test_case['input'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Min Number Of Jumps-----\n')
		assert all_cases_passed

	def test_maximum_sum_submatrix(self):
		print(f'\n-----Maximum Sum Submatrix-----')
		from MaximumSumSubmatrix import main
		test_cases = TestSolutions.read_test_cases('MaximumSumSubmatrix')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.maximum_sum_submatrix(test_case['input']['matrix'], test_case['input']['size'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Maximum Sum Submatrix-----\n')
		assert all_cases_passed

	def test_task_assignment(self):
		print(f'\n-----Task Assignment-----')
		from TaskAssignment import main
		test_cases = TestSolutions.read_test_cases('TaskAssignment')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.task_assignment(test_case['input']['k'], test_case['input']['tasks'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Task Assignment-----\n')
		assert all_cases_passed

	def test_flatten_binary_tree(self):
		print(f'\n-----Flatten Binary Tree-----')
		from FlattenBinaryTree import main
		test_cases = TestSolutions.read_test_cases('FlattenBinaryTree')

		# TODO: can't read weird structure given by website to represent trees
		all_cases_passed = True
		# for test_case in test_cases:
			# result = main.flatten_binary_tree(test_case['input'], test_case['input']['tasks'])

			# all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			# print(f'Inputs: {test_case["input"]};\n\t'
			# 	  f'{Colors.OKCYAN}Expected Output: {test_case["expected_output"]}\n\t'
			# 	  f'{Colors.OKCYAN}Result: {result};\n\t'
			# 	  f'{f"{Colors.OKGREEN}Passed{Colors.WHITE}" if test_case["expected_output"] == result else f"{Colors.FAIL}Failed"}{Colors.WHITE}')

		print('-----Flatten Binary Tree-----\n')
		assert all_cases_passed

	def test_longest_common_subsequence(self):
		print(f'\n-----Longest Common Subsequence-----')
		from LongestCommonSubsequence import main
		test_cases = TestSolutions.read_test_cases('LongestCommonSubsequence')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.longest_common_subsequence(test_case['input']['str1'], test_case['input']['str2'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Longest Common Subsequence-----\n')
		assert all_cases_passed

	def test_four_number_sum(self):
		print(f'\n-----Four Number Sum-----')
		from FourNumberSum import main
		test_cases = TestSolutions.read_test_cases('FourNumberSum')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.four_number_sum(test_case['input']['array'], test_case['input']['targetSum'])

			# TODO: update  check to allow for different ordering of the same nums
			# for quadruplet in result:
			# 	all_cases_passed = all_cases_passed and (set(quadruplet) == )
			all_cases_passed = all_cases_passed and (set(result) == set(test_case['expected_output']))
			TestSolutions.display(test_case, result)
		print('-----Four Number Sum-----\n')
		assert all_cases_passed

	def test_move_element_to_end(self):
		print(f'\n-----Move Element To End-----')
		from MoveElementToEnd import main
		test_cases = TestSolutions.read_test_cases('MoveElementToEnd')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.move_element_to_end(test_case['input']['array'], test_case['input']['toMove'])

			# TODO: this check should be updated to ignore order of elements that are not "toMove"
			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Move Element To End-----\n')
		assert all_cases_passed

	def test_spiral_traverse(self):
		print(f'\n-----Spiral Traverse-----')
		from SpiralTraverse import main
		test_cases = TestSolutions.read_test_cases('SpiralTraverse')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.spiral_traverse(test_case['input'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Spiral Traverse-----\n')
		assert all_cases_passed

	def test_largest_range(self):
		print(f'\n-----Largest Range-----')
		from LargestRange import main
		test_cases = TestSolutions.read_test_cases('LargestRange')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.largest_range(test_case['input'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)
		print('-----Largest Range-----\n')
		assert all_cases_passed

	def test_levenshtein_distance(self):
		print(f'\n-----Levenshtein Distance-----')
		from LevenshteinDistance import main
		test_cases = TestSolutions.read_test_cases('LevenshteinDistance')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.levenshtein_distance(test_case['input']['str1'], test_case['input']['str2'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)

		print('-----Levenshtein Distance-----\n')
		assert all_cases_passed

	def test_zigzag_traverse(self):
		print(f'\n-----Zigzag Traverse-----')
		from ZigzagTraverse import main
		test_cases = TestSolutions.read_test_cases('ZigzagTraverse')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.zigzag_traverse(test_case['input'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			TestSolutions.display(test_case, result)

		print('-----Zigzag Traverse-----\n')
		assert all_cases_passed

