def get_book_words(book_contents):
    number_of_words=0

    number_of_words = len(book_contents.split())

    return number_of_words

def get_book_characters(book_contents):
    lower_contents = book_contents.lower()
    char_dic = {}

    for char in lower_contents:

        if char_dic.get(char) == None:
            char_dic[char]=0

        char_dic[char] += 1
    
    return char_dic
