#!/usr/bin/python

import sys

post_ids = []
old_word = None
word_count = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_word = data_mapped[0]
    post_ids.append(data_mapped[1])

    if old_word and old_word != this_word:
        print old_word, "\t", word_count, "\t", ",".join(sorted(post_ids, keys = lambda x: int(x)))
        old_word = this_word;
        post_ids[:] = []
        word_count = 0

    old_word = this_word
    word_count += 1

if old_word != None:
    print old_word, "\t", word_count, "\t", ",".join(sorted(post_ids, keys = lambda x: int(x)))

