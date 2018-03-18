def reducer():
	total = 0
	old_key = None
	
	for line in sys.stdin:
		data_mapped = line.strip().split("\t")
		if len(data_mapped) != 2:
			continue

		this_key, this_value = data_mapped

		if old_key and old_key != this_key:
			print "{0}\t{1}".format(old_key, total)
			old_key = this_key;
			total = 0

		old_key = this_key
		total += float(this_value)

	if old_key != None:
		print "{0}\t{1}".format(old_key, total)


sys.stdin = open('mapper_result.txt')
sys.stdout = open('reducer_result.txt', 'w')
reducer()
