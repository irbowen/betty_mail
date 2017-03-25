import random
import csv

INSERT_CHARS = [u'\u200A']

# randomly inserts a random char (from INSERT_CHARS) into each word,
# numInserts times, in the input string and returns the new string
def ri(input, numInserts):
	minWordLength = 2
	words = input.split(' ')
	finalWords = []

	for word in words:
		numCharsToInsert = numInserts

		if len(word) <= minWordLength:
			finalWords.append(word)
			continue
		# prevent excessive inserts
		elif len(word) <= numInserts:
			numCharsToInsert = len(word) / 2

		newWord = word
		for i in range(numCharsToInsert):
			# choose a random index to insert char
			randInsertIndex = random.randint(1, len(newWord)-1)
			# choose a random char
			randCharIndex = random.randint(0, len(INSERT_CHARS)-1)
			randChar = INSERT_CHARS[randCharIndex]

			# create new string with insertion
			newWord = newWord[:randInsertIndex] + randChar + newWord[randInsertIndex:]

		finalWords.append(newWord)

	return ' '.join(finalWords)


def get_betty_debt():
	totalDebt = 0
	with open('shame.csv', "r") as database_file:
		reader = csv.DictReader(database_file)
		for row in reader:
			totalDebt += float(row['balance'])
	totalDebt = int(totalDebt) * -1
	return totalDebt
