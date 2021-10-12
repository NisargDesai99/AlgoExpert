import json
# import global_vars
import os


def tournament_winner(competitions, results):

	# TODO: update to use only one for loop instead of two
	# max value/points can be tracked in the same loop

	index = 0
	team_records = {}
	for match in competitions:
		if match[0] in team_records:
			team_records[match[0]] += 0 if results[index] == 0 else 1
		elif match[0] not in team_records:
			team_records[match[0]] = 0 if results[index] == 0 else 1

		if match[1] in team_records:
			team_records[match[1]] += 1 if results[index] == 0 else 0
		elif match[1] not in team_records:
			team_records[match[1]] = 1 if results[index] == 0 else 0

		index += 1

	max_key = ''
	max_value = -1
	for curr_key, curr_value in team_records.items():
		if curr_value > max_value:
			max_key = curr_key
			max_value = curr_value

	return max_key


if __name__ == '__main__':

	test_cases_path = os.path.expanduser('~/Documents/Practice/AlgoExpert/TournamentWinner/test_cases.json')
	# file_path = f'{PROJECT_PATH}/TournamentWinner/test_cases.json'

	test_cases = json.load(open(test_cases_path))
	cases_passed = True

	counter = 1
	for test_case in test_cases:
		winner = tournament_winner(test_case['input']['competitions'], test_case['input']['results'])
		cases_passed = cases_passed and (winner == test_case['expected_output'])
		print(f'case {counter} winner: {winner}')
		counter += 1

	print(f'\nall cases passed: {cases_passed}\n')


