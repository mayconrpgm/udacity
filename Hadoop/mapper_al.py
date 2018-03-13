#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab



import re
import sys

for line in sys.stdin:
	regex = '([(\d\.)]+) (-) (-) \[(.*?)\] "(.*?)" (\d+) ([\d-]+)'
	match = re.match(regex, line)

	if match != None:
		data = match.groups()
		if len(data) == 7:
			ip, customer_id, user_name, time, uri, status_code, bytes = data

			path = uri.split(' ')[1]
			if path.startswith("http://www.the-associates.co.uk"):
				path = path[32:]

			print "{0}\t{1}".format(path, 1)

