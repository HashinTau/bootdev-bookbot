def word_count(text_from_book):
        s = text_from_book.split()
        count = 0
        for words in s:
                if (words != ""):
                        count +=1
        return count

def character_count(text_from_book):
	submit = {}
	f =  list(text_from_book.lower())
	size = len(f)
	count = size
	while count>0:
		letter = f.pop(-1)
		if  (letter in submit):
			submit[letter] +=1
			count-=1
		else:
			submit[letter]=1
			count-=1
	return submit

def sort_on(dict):
    return dict["num"]

def get_sorted_char_counts(count_chars):
    count_chars_list = []
    for key in count_chars:
        count_chars_list.append({"char": key, "num": count_chars[key]})
    count_chars_list.sort(reverse=True, key=sort_on)
    return count_chars_list

def printOut(input, count, sorted_count_characters_list):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {input} ...")
	print("----------- Word Count ----------")
	print(f"Found {count} total words in the document.")
	print("--------- Character Count -------")
	for count_char in sorted_count_characters_list:
		if count_char["char"].isalpha():
			print(f"{count_char["char"]}: {count_char["num"]}")
	print("============= END ===============")
