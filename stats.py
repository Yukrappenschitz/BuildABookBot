def get_book_word_count(book_contents:str) -> int:

    book_contents_list = book_contents.split() #using built in python `.split()` method to turn the string
                                               # into a list of words, delimiter = whitespace (default)

    num_words = len(book_contents_list)     # finding length of list to find number of words

    return num_words

def get_book_text(book: str)-> str:

    with open(book) as book:   # using `with` to open file
        book_contents = book.read()  # using `.read()` method to output the file contents as a string

    return book_contents

def get_book_character_count(book_contents: str) -> dict[str,int]:

    lower_case_book = book_contents.lower() #lowering all characters to avoid duplicates
    list_all_characters = list(lower_case_book)   # using python built in method `list()` to output every character
                                                   # in the string as an element of a list

    # dict setup
    character_dict = {}

    for character in list_all_characters: # iterating through every single character

        if character in character_dict:  # if character is already in dict, just iterate occurrence by 1
            occurrence = character_dict[f"{character}"] # need to fetch occurrence FROM the key[character] before updating by +1

            character_dict[f"{character}"] = occurrence + 1 # updating dict key[character] value occurrence +=1

        else:    # if not in dict, need to add it to keys and set value to 1, as we have hit the character

            character_dict[f"{character}"] = 1

    return character_dict


def sort_on(character_occurrence: tuple[str,int]) -> int:
    # need to return specific character occurrence
    return character_occurrence[1] # since occurrence is stored at index[1] in the tuple

def chars_dict_to_sorted_list(character_dict: dict[str,int]) -> list[tuple[str,int]]:

    character_occurrence_list = [] # empty list to hold all tuples of characters

    for character in character_dict: # iterating through all characters in character_dict

        occurrence = character_dict[character] # fetching occurrence of `"character"` from character_dict

        tuple = (character,occurrence) # creating tuple of `character,occurrence`

        character_occurrence_list.append(tuple) # appending each tuple of character into a list to sort



    sorted_character_occurrence_list = sorted(character_occurrence_list, reverse=True, key=sort_on)

# sorting unsorted character_occurrence_list using built in python method `sorted([target_list], reverse = True, key=sort_on)
#        reverse = True : to sort list from highest to lowest, default: lowest to highest
#  key = sort_on : calls helper function `sort_on` with each `"character"` to fetch each character's occurrence to give to sorted() function
#
    return sorted_character_occurrence_list
