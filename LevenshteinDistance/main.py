
def levenshtein_distance(str1, str2):
    print(str1, '|', str2)

    result = levenshtein_distance_tabulation_optimized_space(str1, str2)
    return result


# time: O(nm) | space: O(min(n,m))
def levenshtein_distance_tabulation_optimized_space(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    large = str1 if len(str1) >= len(str2) else str2

    even_edits = [x for x in range(len(small)+1)]
    odd_edits = [x for x in range(len(small)+1)]

    for i in range(1, len(large)+1):
        if i % 2 == 1:
            current_edits = odd_edits
            prev_edits = even_edits
        else:
            current_edits = even_edits
            prev_edits = odd_edits

        current_edits[0] = i
        for j in range(1, len(small)+1):
            if large[i-1] == small[j-1]:
                current_edits[j] = prev_edits[j-1]
            else:
                current_edits[j] = 1 + min(
                    prev_edits[j-1],
                    prev_edits[j],
                    current_edits[j-1]
                )

    return even_edits[len(small)] if len(large)%2 == 0 else odd_edits[len(small)]


# time: O(nm) | space: O(nm)
def levenshtein_distance_tabulation(str1, str2):
    table = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    for i in range(1, len(str2)+1):
        table[i][0] = table[i-1][0] + 1

    for i in range(1, len(str2)+1):
        for j in range(1, len(str1)+1):
            if str2[i-1] == str1[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(
                    table[i-1][j],
                    table[i][j-1],
                    table[i-1][j-1]
                )

    return table[len(str2)][len(str1)]


if __name__ == '__main__':
    import json
    test_cases = json.load(open('./test_cases.json'))
    for test in test_cases:
        print(f'test: {test}')
        levenshtein_distance(*test['input'])
