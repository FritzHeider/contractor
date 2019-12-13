from dictogram import Dictogram
from random import choice
from analyze import read_file

sample_text = read_file('siddhartha.txt')
markov = {}


def first_order():
	for word in sample_text:
		markov[word] = Dictogram()

	for index in range(len(sample_text) - 1):
		markov[sample_text[index]].add_count(sample_text[index + 1])

	# print(markov['fish'].sample())
	sentence = " "
	word = choice(list(markov.keys()))
	sentence += word
	for i in range(4):
		word = markov[word].sample()
		sentence += " " + word
	# return print(sentence)


def second_order():
	for index in range(len(sample_text) - 2):

		first_word = sample_text[index]
		middle_word = sample_text[index + 1]
		last_word = sample_text[index + 2]

		if (first_word, middle_word) not in markov:
			markov[(first_word, middle_word)] = Dictogram([last_word])
		else:
			markov[(first_word, middle_word)].add_count(last_word)

def get_tuples(word):
	markov = second_order()
	all_tuples = []

	for each_tuple in list(markov):
		if word == each_tuple[0]:
			all_tuples.append(each_tuple)



def generate_sentence():
	markov = second_order()
	word = choice(choice(list(markov)))
	sentence = " " + word
	for i in range(7):
		pair_choice = choice(get_tuples(word))
