import sys

from stats import get_book_word_count
from stats import get_book_text
from stats import get_book_character_count
from stats import chars_dict_to_sorted_list


def main():

    if len(sys.argv) != 2:

        print("Usage: python3 main.py <path_to_book>") #explaining script usage

        sys.exit(1)  # exiting with code `1` 

    book_path = sys.argv[1] # getting bookpath from second input of sys.argv
    
    # book_path = "books/frankenstein.txt" hardcoded path
    # print(get_book_text(book_path)

    book_contents = get_book_text(book_path)

    num_words = get_book_word_count(book_contents)

    num_characters = get_book_character_count(book_contents)

    sorted_num_characters = chars_dict_to_sorted_list(num_characters)

    #print(f"Found {num_words} total words")

    #print(num_characters)

    #print(sorted_num_characters)

    print_report(book_path, num_words, sorted_num_characters)

def print_report(book_path:str, word_count:int, sorted_list_character:list[tuple(str,int)]):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for character in sorted_list_character:

        if character[0].isalpha() == True:
            print(f"{character[0]}: {character[1]}")

    print("============= END ===============")

main()
