text_1 = "toi mua me con bo con cua con ban toi"

text_2 = "toi mua con con bo me cua con ban toi"

library = []

def compare_text(text_input, text_compare):
	text_input = text_input.split()
	text_compare = text_compare.split()

	def collect_lib(text_input):
		for i in range(0, len(text_input)-1):
			if text_input[i] not in library:
				library.append(text_input[i],len(library)+1)
		return library

	print collect_lib(text_input)

	def unique_word(text_input):
		unique = []
		for i in range(0, len(text_input)-1):
			if text_input[i] not in unique:
				unique.append(text_input[i])
		return unique

	unique_text = unique_word(text_input)

	def compare(unique_text, text_compare):
		total = 0
		for i in range(0, len(unique_text)-1):
			count = text_compare.count(unique_text[i])
			print "The word", unique_text[i] , "displays %i times" % count
			if count > 0:
				total += 1
		return total
	# total = compare(unique_text, text_compare)
	return compare(unique_word(unique_text),text_compare)

compare_text(text_1, text_2)
