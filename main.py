from stats import get_book_words
from stats import get_book_characters

def get_book_text(filepath):
    
    file_contents=""

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    book_contents = get_book_text("./books/frankenstein.txt")
    num_words = get_book_words(book_contents)
    print(f"Found {num_words} total words")
    print(get_book_characters(book_contents))

main()