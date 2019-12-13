
def read_file(file):
	with open(file) as book:
		data = book.readlines()

	words = [word.strip(" ' , @ $ , \t \n ").lower() for word in data]
	text_to_use = ' '.join(words)

	words_list = text_to_use.split(' ')
	return words_list


def calculate_histogram_dict(source_text):
	words_list = read_file(source_text)

	text_dict = {}
	for word in words_list:
		text_dict[word] = 0
	for word in words_list:
		text_dict[word] += 1
	return text_dict


def unique_words(histogram):
	return len(histogram)


def frequency(word, histogram):
	if histogram[word]:
		return histogram[word]
	else:
		return f'No Such Word'


def calculate_histogram_lists(source_text):
	histogram = []
	text_dict = calculate_histogram_dict(source_text)
	for k, v in text_dict.items():
		histogram.append([k, v])
	return print(histogram)


def calculate_histogram_tuples(source_text):
	histogram = []
	text_dict = calculate_histogram_dict(source_text)
	for k, v in text_dict.items():
		histogram.append((k, v))
	return print(histogram)


print(calculate_histogram_dict('siddhartha.txt'))
