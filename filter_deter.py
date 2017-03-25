import random
import csv

INSERT_CHARS = [u'\u200A']

# randomly inserts a random char (from INSERT_CHARS) into each word in the input
# and returns the string
def ri(input):
	minWordLength = 2
	words = input.split(' ')
	finalWords = []

	for word in words:
		if len(word) <= minWordLength:
			finalWords.append(word)
			continue
		# choose a random index to insert char
		randInsertIndex = random.randint(1, len(word)-1)
		# choose a random char
		randCharIndex = random.randint(0, len(INSERT_CHARS)-1)
		randChar = INSERT_CHARS[randCharIndex]

		# create new string with insertion
		newStr = word[:randInsertIndex] + randChar + word[randInsertIndex:]

		finalWords.append(newStr)

	return ' '.join(finalWords)


def get_betty_debt():
	totalDebt = 0
	with open('shame.csv', "r") as database_file:
		reader = csv.DictReader(database_file)
		for row in reader:
			totalDebt += float(row['balance'])
	totalDebt = int(totalDebt) * -1
	return totalDebt
