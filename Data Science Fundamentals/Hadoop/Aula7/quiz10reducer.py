#!/usr/bin/python

import sys

sales_total = 0
sales_count = 0
old_key = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 3:
		# Something has gone wrong. Skip this line.
		continue

	this_key, this_sale, this_count = data_mapped

	if old_key and old_key != this_key:
		print old_key, "\t", sales_total , "\t", sales_count
		old_key = this_key;
		sales_total = 0
		sales_count = 0

	old_key = this_key
	sales_total += float(this_sale)
	sales_count += float(this_count)

if old_key != None:
	print old_key, "\t", sales_total , "\t", sales_count

