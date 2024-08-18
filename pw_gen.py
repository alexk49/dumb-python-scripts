"""
Extremely inefficient Password generator based off of the logic of this xkcd comic:https://xkcd.com/936/, created using standard python libraries.

"""
from os import path
from secrets import randbelow, choice
import string
import sys

WORDS = r"/usr/share/dict/words"


def generate_word_by_index(words):
    """function takes list of words
    expected use is lines from readlines
    after opening of a text file
    """
    index = randbelow((len(words) + 1))
    # return word and clean output
    return words[index]


def check_word_length(word, words, generator):
    """check word for suitable length"""
    while len(word) < 4:
        if generator == "index":
            word = generate_word_by_index(words)
        else:
            word = choice(words).strip()
    return word


def remove_apostrophes(word):
    """remove punctuation from random words"""
    word = word.replace("'", "")
    return word


def main():
    """main function
    check if words file exists
    read words file
    generate random number to index file
    write line to password
    repeat until password long enough
    """

    if not path.exists(WORDS):
        print("Words file not found. Please get a Linux system")
        sys.exit(1)

    with open(WORDS, "r", encoding="utf8") as file:
        # generate words list
        words = [word.strip() for word in file]
    # assign first word
    first_word = generate_word_by_index(words)
    first_word = check_word_length(first_word, words, "index")
    first_word = remove_apostrophes(first_word)

    # generate second word
    second_word = choice(words)
    second_word = check_word_length(second_word, words, "choice")
    second_word = remove_apostrophes(second_word)

    third_word = generate_word_by_index(words)
    third_word = check_word_length(third_word, words, "index")
    third_word = remove_apostrophes(third_word)

    fourth_word = choice(words)
    fourth_word = check_word_length(fourth_word, words, "choice")
    fourth_word = remove_apostrophes(fourth_word)

    # add random punctuation mark to end of password
    index = randbelow(len(string.punctuation))
    mark = string.punctuation[index]

    # add random 2 digit number to end of password
    digit = str(randbelow(99))

    password = first_word + " " + second_word + " " + third_word + " " + fourth_word + mark + digit
    print(password)


if __name__ == "__main__":
    main()
