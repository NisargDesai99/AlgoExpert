


def validIPAddresses(string):

	if len(string) <= 3:
		return []

	addresses = []
	return addresses


string = "1921680"
result = validIPAddresses(string)
print(f'input: {string}; result: {result}')


"""

1921680

first_pos: int
second_pos: int
third_pos: int
list of valid position tuples: [(first, second, third)]

1.9.2.1680 - invalid move over one
1.9.21.680 - 680 invalid move over one
1.9.216.80

1.92.16.80
1.92.168.0

19.2.1.680 - invalid; move third over one
19.2.16.80
19.2.168.0
19.21.68.0 - move second pos over; since third can't be moved over anymore
19.21.6.80




"1.9.216.80"
"1.92.16.80"
"1.92.168.0"
"19.2.16.80"
"19.2.168.0"
"19.21.6.80"
"19.21.68.0"
"19.216.8.0"
"192.1.6.80"
"192.1.68.0"
"192.16.8.0"



Givens:
	- string of len 12 or smaller
	- contains only digits

Return:
	- all possible IP addresses that can be created by inserting 3 '.'s in the string

IP address
	- a sequence of 4 positive integers that are separated by '.' where each individual integer 
	is within the range 0-255, inclusive... [0,255]
	- Leading 0s in an IP address makes it invalid: 
		* 192.168.00.1 - invalid because of '00'
		* 192.168.0.01 - invalid because of '01'
		* 991.1.1.0 - invalid because 991 > 255
		
	




"""

