
import json


def validate_subsequence(array, sequence):
	seq_idx = 0
	for i in range(len(array)):
		if seq_idx == len(sequence):
			break
		if sequence[seq_idx] == array[i]:
			seq_idx += 1
	return seq_idx == len(sequence)


if __name__ == '__main__':
    print('Validate Subsequence')

    json_inputs = json.load(open('./inputs.json'))
    for item in json_inputs:
        is_subsequence = validate_subsequence(item['array'], item['sequence'])
        print(f'arr: {item["array"]}; seq: {item["sequence"]} == {is_subsequence}')
