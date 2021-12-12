def is_whitespace(char):
	if char == '\n' or char == '\t' or char == ' ':
		return char
	else:
		return ''


def reverse_words_in_string(s):
	reversed_s = ''
	curr_word_start_idx = len(s)
	curr_word_end_idx = len(s)

	for i in range(len(s) - 1, -1, -1):
		whitespace_char = is_whitespace(s[i])
		if len(whitespace_char) == 0:
			curr_word_start_idx -= 1
		else:
			reversed_s = f'{reversed_s}{s[curr_word_start_idx:curr_word_end_idx]}{whitespace_char}'
			curr_word_end_idx = i
			curr_word_start_idx -= 1

	return f'{reversed_s}{s[curr_word_start_idx:curr_word_end_idx]}'

