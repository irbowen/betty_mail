#!/usr/bin/python3

with open('shame.csv') as f:
    lines = f.readlines()[1:]

for line in lines:
    line = line.strip('\n')
    words = line.split(',')
    # Ignore those on the wall of shame less than a week
    if (int(words[3]) < 7):
        continue
    print("%s,%s,%s,%s" % (words[0], words[1], words[2], words[3]))

