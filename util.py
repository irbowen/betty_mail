#!/usr/bin/python3

f = open('shame.csv')
lines = f.readlines()[1:]

for line in lines:
    line = line.strip('\n')
    words = line.split(',')
    unique_name = words[0]
    email = unique_name + "@umich.edu"
    # Ignore those on the wall of shame less than a week
    if (int(words[3]) < 7):
        continue
    print("%s,%s,%s,%s" % (email, words[1], words[2], words[3]))

