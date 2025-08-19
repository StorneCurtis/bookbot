from stats import count_words
from stats import count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def main():
    print(count_words("books/frankenstein.txt"))
    print(count_characters("books/frankenstein.txt"))

#    get_book_text("books/frankenstein.txt")

main()