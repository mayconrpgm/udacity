import sys

def mapper():
	for line in sys.stdin:
		data = line.strip().split(",")
		if len(data) == 22 and data[1] != 'UNIT':
			print "{0}\t{1}".format(data[1], data[6])


sys.stdin = open('turnstile_data_master_with_weather.csv')
sys.stdout = open('mapper_result.txt', 'w')
mapper()