def get_book_text(filepath):
    
    file_contents=""

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_book_words(book_contents):
    number_of_words=0

    number_of_words = len(book_contents.split(' '))

    return number_of_words

def main():
    num_words = get_book_words(get_book_text("./books/frankenstein.txt"))
    print(f"Found {num_words} total words")

main()