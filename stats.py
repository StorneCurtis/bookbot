from collections import Counter

def count_words(path_to_file):
    file_length = 0
    with open(path_to_file) as f:
        file_Contents = f.read()
        file_words = file_Contents.split()
        file_length = len(file_words)
        return (f"{file_length} words found in the document")

def count_characters(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read().lower()
        total_characters = len(file_contents)
        cntr = Counter(file_contents)
        return (cntr)

