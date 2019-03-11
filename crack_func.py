import hash_cracker_joshua
import settings
import time
import hashlib

# Function to make output file if requested
def make_output_file(word):
	try:
		f = open(current_output_file + '.txt', 'x')
	except FileExistsError:
		exists = input('File already exists, replace it? (y/n) ')
		if exists == 'y' or exists == 'Y':
			f = open(current_output_file + '.txt', 'w+')
			f.write('Word is: {}'.format(word))
			f.close()
			print('\nEverything was written to file succesfully!')
		elif exists == 'n' or exists == 'N':
			print('Please change the output file name in settings')	
	else:
		f.write('Word is: {}'.format(word))
		f.close()

def general(verbose, salt, words, hash_to_crack, chosen_algorithm, output_file):

	print('In general', hash_to_crack)
	print('Salt: ', salt)

	hash_to_crack = hash_cracker_joshua.getInput('Hash to crack')

	n = 0

	start = time.time()

	for i in words:
		n += 1
		j = bytes(i + salt, 'utf-8')
		hashed = getattr(hashlib, chosen_algorithm)(j).hexdigest()
		# Verbose could be checked here and improve readability but would likely slow down the program
		# if verbose is True:
		print(hashed) # This is the only extra line for verbose... How can it be improved?
		if hashed == hash_to_crack:
			end = time.time()
			print('\nHash found, the password is: ', i)
			print('\nTime took to complete: ', (end-start))
			print('Words tried: ', n)
			if output_file:
				make_output_file(i)
				break
			else:
				break

# Crack hash without input file or verbose
def simple_crack(chosen_algorithm, output_file=False):

	n = 0

	hash_to_crack = input('Hash to crack: ').lower()
	salt = input('Salt: ')

	# Loop over dictionary file
	general(verbose, salt, words, hash_to_crack, chosen_algorithm, output_file)