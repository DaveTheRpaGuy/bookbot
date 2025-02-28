def count_words(file_contents):
    return len(file_contents.split())

def count_chars(file_contents):
    characters = {}
    for char in file_contents.lower():
        if char.isalpha() == False:
            continue
        
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_chars(characters):
    char_counts_dict_list = []
    for k in characters:
        char_counts_dict_list.append({"char": k, "num": characters[k]})
    char_counts_dict_list.sort(reverse=True, key=sort_on)
    return char_counts_dict_list

def sort_on(dict):
    return dict["num"]