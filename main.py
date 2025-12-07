from stats import get_book_words

def get_book_text(filepath):
    
    file_contents=""

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents



def main():
    num_words = get_book_words(get_book_text("./books/frankenstein.txt"))
    print(f"Found {num_words} total words")

main()