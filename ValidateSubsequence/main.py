def validate_subsequence(array, sequence):
	seq_idx = 0
	for i in range(len(array)):
		if seq_idx == len(sequence):
			break
		if sequence[seq_idx] == array[i]:
			seq_idx += 1
	return seq_idx == len(sequence)
