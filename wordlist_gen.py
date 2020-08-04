import sys
import getopt
import string
from itertools import product


EXCEPTION_COLOR = '\033[91m'
END_COLOR = '\x1b[0m'

save_to_file = False
filename = ""
min_len = 0
max_len = 0
char_set = string.ascii_letters + string.digits + string.punctuation
help_text = """wordlist-generator 0.1 ( https://github.com/nicolai-h/wordlist-generator )
USAGE:
wordlist-generator -s <min_len> -l <max_len> [options]
OPTIONS:
-s, --shortest: specify minimum length of generated words
-l, --longest: specify maximum length of generated words
-c, --character-set: specify the character set used for generating the words
-o, --output: specify the file where the generated words should be stored
-h, --help: get help info
DEFAULTS:
minimum length: 0
maximum length: 0
character set: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 
output: by default the generated words will be printed out to the terminal
EXAMPLE USAGE:
python3 wordlist_gen.py -s 2 -l 4 -c abcd -o test.txt
"""


def gen_wordlist(argv):
	global save_to_file
	global filename
	global min_len
	global max_len
	global char_set
	global help_text

	if len(argv) == 0:
		print(help_text)
		sys.exit()
	try:
		opts, args = getopt.getopt(argv, "s:l:c:o:h", ["shortest=", "longest=", "character-set=", "output=", "help"])
	except getopt.GetoptError:
		print(EXCEPTION_COLOR + "generate_wordlist --shortest <min_len> --longest <max_len> --character-set <char_set> --output <output_file>" + END_COLOR)
		sys.exit()

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			print(help_text)
			sys.exit()
		elif opt in ("-o", "--output"):
			save_to_file = True
			filename = arg
		elif opt in ("-c", "--character-set"):
			char_set = arg
		elif opt in("-s", "--shortest"):
			try:
				min_len = int(arg)
			except ValueError:
				print(EXCEPTION_COLOR + "minimum length needs to be a number" + END_COLOR)
				sys.exit()
		elif opt in ("-l", "--longest"):
			try:
				max_len = int(arg)
			except ValueError:
				print(EXCEPTION_COLOR + "maximum length needs to be a number" + END_COLOR)
				sys.exit()


def create_wordlist():
	diff_len = max_len - min_len
	if save_to_file == True:
		with open(filename, 'w') as f:
			for i in range(max_len-min_len+1):
				for ele in product(char_set, repeat=min_len+i):
					f.write(''.join(ele) + '\n')
	else:
		for i in range(max_len-min_len+1):
			for ele in product(char_set, repeat=min_len+i):
				print(''.join(ele))


if __name__ == "__main__":
	gen_wordlist(sys.argv[1:])
	create_wordlist()
