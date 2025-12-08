from stats import get_book_words
from stats import get_book_characters
from stats import pretty_dictionary_report
import sys

def get_book_text(filepath):
    
    file_contents=""

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    num_words = get_book_words(book_contents)
    sorted_report = pretty_dictionary_report(get_book_characters(book_contents))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dic in sorted_report:
        print(f"{dic["name"]}: {dic["num"]}")

    print("============= END ===============")

main()