#!/usr/bin/python

# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

def reducer():
	old_id = None
	post_id = None
	title = None
	tagnames = None
	author_id = None
	node_type = None
	parent_id = None
	abs_parent_id = None
	added_at = None
	score = None
	reputation = None
	gold = None
	silver = None
	bronze = None

	reader = csv.reader(sys.stdin, delimiter='\t')
	for data_mapped in reader:	
		this_id = data_mapped[0]

		if old_id and old_id != this_id:
			print post_id, "\t", title, "\t", tagnames, "\t", author_id, "\t", node_type, "\t", parent_id, "\t", abs_parent_id, "\t", added_at, "\t", score, "\t", reputation, "\t", gold, "\t", silver, "\t", bronze

		if(data_mapped[1] == "A"):
			reputation = data_mapped[2] 
			gold = data_mapped[3]
			silver = data_mapped[4]
			bronze = data_mapped[5]
		
		if(data_mapped[1] == "B"):
			author_id = data_mapped[0]
			post_id = data_mapped[2]
			title = data_mapped[3]
			tagnames = data_mapped[4]
			node_type = data_mapped[5]
			parent_id = data_mapped[6] 
			abs_parent_id = data_mapped[7]
			added_at = data_mapped[8]
			score = data_mapped[9]

		old_id = this_id

	if old_id != None:
		print post_id, "\t", title, "\t", tagnames, "\t", author_id, "\t", node_type, "\t", parent_id, "\t", abs_parent_id, "\t", added_at, "\t", score, "\t", reputation, "\t", gold, "\t", silver, "\t", bronze


reducer()