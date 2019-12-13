import random


def histogram(words):
	words_list = words.split(' ')
	text_dict = {}
	for word in words_list:
		text_dict[word] = 0
	for word in words_list:
		text_dict[word] += 1
	return text_dict


def sample(histogram):
	dart = random.random()
	total_values = 0
	for value in histogram.values():
		total_values += value
	total = 0
	for word in histogram:
		individual_probability = histogram[word] / total_values
		if total < dart <= total + individual_probability:
			return word
		else:
			total += individual_probability


def test_sample(histogram):
	total_words = [sample(histogram) for _ in range(10000)]
	fish_count = 0
	one_count = 0
	two_count = 0

	for word in total_words:
		if word == 'fish':
			fish_count += 1
		elif word == 'one':
			one_count += 1
		elif word == 'two':
			two_count += 1
	print(fish_count, one_count, two_count)


test_sample(histogram('one two fish'))
