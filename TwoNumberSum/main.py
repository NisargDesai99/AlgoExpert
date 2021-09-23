

def two_number_sum(target_sum: int, arr=[]):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target_sum:
            return [arr[left], arr[right]]
        elif curr_sum < target_sum:
            left += 1
        elif curr_sum > target_sum:
            right -= 1
    return []


if __name__ == '__main__':
    print('Two Number Sum')

    input_arr = [int(item) for item in input('Enter the list: ').split()]
    target_sum = int(input('Enter target sum: '))

    result = two_number_sum(target_sum, input_arr)
    print(f'Result: {result}')


# Test input:
#   3 5 -4 8 11 1 -1 6              original
#   -4 -1 1 3 5 6 8 11              sorted

