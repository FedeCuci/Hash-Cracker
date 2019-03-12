import random
import hashlib
import os
import time
import settings
import crack_func

def getInput(text):
	try:
		choice = input('{}> '.format(text))
	except KeyboardInterrupt:
		print('')
		exit()
	return choice

def algorithm_option(val):
	pass

actions = {
	'settings': settings,
	'1' : algorithm_option,
	'2': algorithm_option,
	'3' : algorithm_option
}

# cmd = input('Enter Command: ')

# if cmd in actions.keys:
# 	actions[cmd](val)

#Welcome message to display when file is run
welcome = '''
 _   _           _       _____                _             
| | | |         | |     /  __ \              | |            
| |_| | __ _ ___| |__   | /  \/_ __ __ _  ___| | _____ _ __ 
|  _  |/ _` / __| '_ \  | |   | '__/ _` |/ __| |/ / _ \ '__|
| | | | (_| \__ \ | | | | \__/\ | | (_| | (__|   <  __/ |   
\_| |_/\__,_|___/_| |_|  \____/_|  \__,_|\___|_|\_\___|_|   
                                                            
For a list of commands, type: "help"
                                                            '''

# Global variables
os.system('clear') # Clear the screen
print(welcome)

current_algorithm = ''
current_salt = ''
current_dictionary = '/usr/share/dict/words'
current_output_file = ''
hash_to_crack = ''
output_file = ''
verbose = False
input_file = ''
supported_algorithms = ['MD5', 'md5', 'SHA256', 'sha256', 'SHA512', 'sha512']

# Print out the current status of settings
def status():
	print('\nDictionary file: ', current_dictionary)
	print('Algorithm: ', current_algorithm)
	print('Verbose: ', str(verbose))
	print('Output file: ', current_output_file)
	print('Input file: ', current_input_file, '\n')

help_info = '''
 Crack: crack your hash/es with current settings
 Settings: change your settings
 Status: Get an overview of your current settings
	'''
	
def main(verbose=False, dictionary='/usr/share/dict/words', salt='', input_file='', hash_to_crack='', chosen_algorithm='', output_file=False):

	words = open(current_dictionary).read().splitlines()

	while True: 
		
		beginning = getInput('')
		if beginning == 'help':
			print(help_info)
		elif beginning == 'settings':
			print('''
	Type: "help" + "command name" for a list of available options.
	1. Algorithm
	2. Dictionary
	3. Verbose
	4. Input file
	5. Output file
	6. Salt\n''')

			settings.settings(verbose, dictionary, salt, words, hash_to_crack, chosen_algorithm, output_file)

			# Change settings category 
			
		elif beginning == 'crack':

			crack_func.general(verbose, dictionary, salt, words, hash_to_crack, chosen_algorithm, output_file)

			# # Run crack() based on algorithm
			# if chosen_algorithm in supported_algorithms:
			# 	crack(chosen_algorithm, verbose, input_file, output_file)
			# else:
			# 	print('You must choose a hashing algorithm in: settings/algorithm')

		elif beginning == 'algorithms':
			print(supported_algorithms)
		elif beginning == 'clear':
			os.system('clear')
			print(welcome)
		elif beginning == 'c':
			exit()
		elif beginning == 'status':
			status()
			
		elif beginning == 'info':
			print('''
	Hash cracker takes a hash and appends the provided salt to it.
	After that, it loops through a dictionary file and hashes 
	every single word using the hash algorithm provided. After
	each hash, it checks whether it matches the hash to be cracked.\n''')
		else:
			print('Unknown command')

if __name__ =='__main__':
	main(verbose, current_dictionary, current_salt, input_file, hash_to_crack, current_algorithm, output_file)