from stats import count_words, count_characters, sort_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def main():
    book_path = "books/frankenstein.txt"
    word_count = count_words(book_path)
    character_count = count_characters(book_path)
    sorted_characters = sort_dictionary(count_characters(book_path))
    #print(word_count)
    #print(character_count)
    #print(sorted_characters)
    print(f"""============ BOOKBOT ============
Analyzing book found at {book_path}
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for c in sorted_characters:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")

main()