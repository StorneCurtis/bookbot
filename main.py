def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def count_words(path_to_file):
    file_length = 0
    with open(path_to_file) as f:
        file_Contents = f.read()
        file_words = file_Contents.split()
        file_length = len(file_words)
    print (f"{file_length} words found in the document")





def main():
    count_words("books/frankenstein.txt")
#    get_book_text("books/frankenstein.txt")

main()