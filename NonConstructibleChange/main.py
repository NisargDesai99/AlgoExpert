import os
import json
import unittest


"""
Time complexity     = O(nlogn)
Space complexity    = O(1)
"""
def non_constructible_change(coins):
    coins.sort()

    curr_sum = 0
    for item in coins:
        if curr_sum + 1 < item:
            return curr_sum + 1
        curr_sum += item
    return curr_sum + 1


class NonConstructibleChange(unittest.TestCase):

    def test_non_constructible_change(self):
        min_change = non_constructible_change([1,3,5,7,10])
        print(f'non-constructible change: {min_change}')

        test_cases_file = open('./inputs.json')
        test_cases = json.load(test_cases_file)
        test_cases_file.close()

        cases_passed = True
        counter = 1
        for test_case in test_cases:
            result_change = non_constructible_change(test_case['coins'])
            cases_passed = cases_passed and (result_change == test_case['expected_output'])
            print(f'case {counter} - computed result: {result_change}')
            counter += 1
        assert cases_passed







