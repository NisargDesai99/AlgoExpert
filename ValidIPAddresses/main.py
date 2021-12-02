

def is_valid_ip_component(s):
	s_as_int = int(s)
	if s_as_int > 255 or s_as_int < 0:
		return False

	return len(s) == len(str(s_as_int))


def validIPAddresses(string):

	addresses = []

	counter = 0
	for first in range(1, min(len(string), 4)):
		first_part = string[0:first]
		if not is_valid_ip_component(first_part):
			continue

		for second in range(first+1, first + min(len(string) - first, 4)):
			second_part = string[first:second]
			if not is_valid_ip_component(second_part):
				continue

			for third in range(second+1, second + min(len(string) - second, 4)):
				third_string = string[second:third]
				fourth_string = string[third:]
				ip_address = ''

				if is_valid_ip_component(third_string) and is_valid_ip_component(fourth_string):
					ip_address = string[0:first] + '.' + string[first:second] + '.' + string[second:third] + '.' + string[third:]
					addresses.append(ip_address)

				print(f'{counter}:: {first}; {second}; {third} -- {ip_address}')

				counter += 1

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

