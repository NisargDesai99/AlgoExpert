
def levenshtein_distance(str1, str2):
    print(str1, '|', str2)
    
    
    return



import json
test_cases = json.load(open('./test_cases.json'))
for test in test_cases:
    print(f'test: {test}')
    levenshtein_distance(*test['input'])


