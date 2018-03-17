#!/usr/bin/python

import re

line = '10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET http://www.the-associates.co.uk/teste HTTP/1.1" 403 202'
regex = '([(\d\.)]+) (-) (-) \[(.*?)\] "(.*?)" (\d+) ([\d-]+)'


match = re.match(regex, line)

if match != None:
	data = match.groups()
	if len(data) == 7:
		ip, customer_id, user_name, time, uri, status_code, bytes = data
		path = uri.split(' ')

		print data
		print path[1]