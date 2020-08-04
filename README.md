# wordlist-generator

## Usage
wordlist-generator -s <min_len> -l <max_len> [options]

## Options
-s, --shortest: specify minimum length of generated words

-l, --longest: specify maximum length of generated words

-c, --character-set: specify the character set used for generating the words

-o, --output: specify the file where the generated words should be stored

-h, --help: get help info

## DEFAULTS
minimum length: 0

maximum length: 0

character set: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 

output: by default the generated words will be printed out to the terminal

## EXAMPLE USAGE
generate-wordlist -s 2 -l 4 -c abcd -o test.txt
