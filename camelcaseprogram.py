  
def camelcase(sentence):
	""" Convert sentence to camelCase, for example, "Display all books" 
	is converted to "displayAllBooks" """
	title_case = sentence.title() # Uppercase first letter of each word
	upper_camel_cased = title_case.replace(' ', '') # getting rid of spaces
	# Lowercase first letter, join with rest of string 
	# Slices don't produce index out of bounds errors. 
	# So this still works on empty strings, strings of length 1
	return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def banner():
	""" Display program name in banner """
	message = 'CAMELCASE PROGRAM!!!!'
	stars = '*' * len(message)
	print(f'\n {stars} \n {message} \n {stars}\n') 

def instructions():
	print("Enter a sentence to convert to Camelcase")


def main():
	banner()
	instructions()
	print("Welcome to camelcase converter")
	sentence = input('Enter your sentence: ')
	output = camelcase(sentence)
	print(output)
if __name__ == '__main__':
	main()