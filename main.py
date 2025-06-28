from stats import word_count, character_count, printOut, get_sorted_char_counts
import sys

def get_book_text(path_to_file):
	with open(path_to_file, encoding='latin-1') as f:
		file_contents = f.read()
	return file_contents

def main():
	input = sys.argv[1]
	g = get_book_text(input) #book content generation
	h = word_count(g) #word count of book
	t =  character_count(g) #letter counts
	sorted_count_characters_list = get_sorted_char_counts(t) #Sorting the letters
	printOut(input, h, sorted_count_characters_list)


if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 
    main()
