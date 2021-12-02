
import os
import json
import unittest
import global_vars
from trees import BinarySearchTree

class TestSolutions(unittest.TestCase):

	def read_test_cases(self, problem_dir):
		print(f'read test cases')
		path = f'{global_vars.PROJECT_PATH}/{problem_dir}/test_cases.json'
		test_cases_file = open(path)
		test_cases = json.load(test_cases_file)
		test_cases_file.close()

		return test_cases


	def test_non_constructible_change(self):
		print('\n-----Non-ConstructibleChange-----')
		from NonConstructibleChange import main

		test_cases = self.read_test_cases('NonConstructibleChange')

		all_cases_passed = True
		counter = 1
		for test_case in test_cases:
			result_change = main.non_constructible_change(test_case['coins'])

			all_cases_passed = all_cases_passed and (result_change == test_case['expected_output'])

			print(f'Input {test_case["coins"]};\n\t'
				  f'Result: {result_change}; {"Passed" if result_change == test_case["expected_output"] else "Failed"}')
			counter += 1

		print('-----Non-ConstructibleChange-----\n')
		assert all_cases_passed


	def test_validate_subsequence(self):
		print('\n-----Validate Subsequence-----')
		from ValidateSubsequence import main

		test_cases = self.read_test_cases('ValidateSubsequence')

		all_cases_passed = True
		for test_case in test_cases:
			is_subsequence = main.validate_subsequence(test_case['array'], test_case['sequence'])
			print(f'arr: {test_case["array"]}; seq: {test_case["sequence"]};\n\t'
				  f'Result: {is_subsequence}; '
				  f'{"Passed" if test_case["expected_output"] == is_subsequence else "Failed"}')
			all_cases_passed = all_cases_passed and (test_case['expected_output'] == is_subsequence)

		print('-----Validate Subsequence-----\n')
		assert all_cases_passed


	def test_sorted_squared_array(self):
		print('\n-----Sorted Squared Array-----')
		from SortedSquaredArray import main

		test_cases = self.read_test_cases('SortedSquaredArray')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.sorted_squared_array(test_case['array'])

			all_cases_passed = all_cases_passed and (test_case['expected_output'] == result)
			print(f'Input Array: {test_case["array"]};\n\t'
				  f'Result: {result}; {"Passed" if test_case["expected_output"] == result else "Failed"}')

		print('-----Sorted Squared Array-----\n')
		assert all_cases_passed


	def test_tournament_winner(self):
		print('\n-----Tournament Winner-----')
		from TournamentWinner import main

		test_cases = self.read_test_cases('TournamentWinner')

		all_cases_passed = True
		for test_case in test_cases:
			winner = main.tournament_winner(test_case['input']['competitions'], test_case['input']['results'])

			all_cases_passed = all_cases_passed and (winner == test_case['expected_output'])
			print(f'Competitions: {test_case["input"]["competitions"]}; Results: {test_case["input"]["results"]}\n\t'
				  f'Winner: {winner}; {"Passed" if test_case["expected_output"] == winner else "Failed"}')

		print('-----Tournament Winner-----\n')
		assert all_cases_passed


	def test_closest_value_bst(self):
		print('\n-----Closest Value BST-----')
		from ClosestValueBST import main
		test_cases = self.read_test_cases('ClosestValueBST')
		# TEST CASES BST INPUTS IN PRE-ORDER
		# TODO: create BST with pre-order traversal

		all_cases_passed = True
		for test_case in test_cases:
			bst = BinarySearchTree()
			bst.build_from_list(test_case['input'])
			target = test_case['target']

			result = main.closest_value_bst(bst, target)

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			print(f'Inputs: {test_case["input"]}; Expected Output: {test_case["expected_output"]}\n\t'
				  f'Result: {result}; {"Passed" if test_case["expected_output"] == result else "Failed"}')

		print('-----Closest Value BST-----\n')
		assert all_cases_passed


	# TODO: finish tests
	def test_branch_sum(self):
		print('\n-----Branch Sums-----')
		from BranchSums import main
		test_cases = self.read_test_cases('BranchSums')

		for test_case in test_cases:
			continue

		print('-----Branch Sums-----\n')
	

	# TODO: finish tests for BST
	# def test_bst_insert()
	# def test_bst_remove()
	# def test_bst_contains()

	def test_validate_bst(self):
		print(f'\n-----Validate BST-----')
		from ValidateBST import main
		test_cases = self.read_test_cases('ValidateBST')

		for test_case in test_cases:
			continue

		print('-----Branch Sums-----\n')


	def test_remove_islands(self):
		print(f'\n-----Remove Islands-----')
		from RemoveIslands import main
		test_cases = self.read_test_cases('RemoveIslands')

		all_cases_passed = True
		for test_case in test_cases:
			result = main.remove_islands(test_case['input'])

			all_cases_passed = all_cases_passed and (result == test_case['expected_output'])
			print(f'Inputs: {test_case["input"]}; Expected Output: {test_case["expected_output"]}\n\t'
				  f'Result: {result}; {"Passed" if test_case["expected_output"] == result else "Failed"}')

		print('-----Remove Islands-----\n')
		assert all_cases_passed
