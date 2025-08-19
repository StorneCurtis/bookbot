def count_words(path_to_file):
    file_length = 0
    with open(path_to_file) as f:
        file_Contents = f.read()
        file_words = file_Contents.split()
        file_length = len(file_words)
        return (len(file_words))
    
def count_characters(path_to_file):
    char_dict = {}
    with open(path_to_file) as f:
        file = f.read().lower()
        for c in file:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
        return char_dict
    
def sort_on(items):
    return items["num"]

def sort_dictionary(dict):
    characters = []
    for c in dict:
        if c.isalpha():
            temp_dict = {}
            temp_dict["char"] = c
            temp_dict["num"] = dict[c]
            characters.append(temp_dict)
    characters.sort(reverse=True,key=sort_on)
    
    #print(characters)
    return characters