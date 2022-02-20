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
