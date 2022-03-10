



def levenshtein_distance(str1, str2):
	print(str1, '|', str2)




import json
test_cases = json.load(open('./test_cases.json'))
for test in test_cases:
	levenshtein_distance(*test['input'])


