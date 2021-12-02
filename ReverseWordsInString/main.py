def is_whitespace(char):
	return char == '\n' or char == '\t' or char == ' '

def reverse_words_in_string(s):
	reversed_s = ''
	
	curr_word_start_idx = 0
	for i in range(len(s) - 1, -1, -1):
		whitespace_char = is_whitespace()
		if not is_whitespace(s[i]):
			curr_word += s[i]
			# print(f'curr_word: {curr_word}')
		else:
			print(f'found whitespace - curr reversed_s: {reversed_s}; curr_word: {curr_word}')
			reversed_s = f'{reversed_s}{curr_word}{whitespace_char}'
			curr_word = ''

	return reversed_s


s = 'tim is great'
result = reverse_words_in_string(s)
print(f'{s}: {result}')

# s2 = 'whitespaces    4'
# result2 = reverse_words_in_string(s2)
# print(f'{s2}: {result2}')
