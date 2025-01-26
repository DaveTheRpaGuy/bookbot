def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    char_counts = count_chars(file_contents)
    char_counts_dict_list = []
    for k in char_counts:
        char_counts_dict_list.append({"char": k, "num": char_counts[k]})
    
    print(char_counts_dict_list)

    char_counts_dict_list.sort(reverse=True, key=sort_on)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char_count in char_counts_dict_list:
        print(f"The '{char_count["char"]}' character was found {char_count["num"]} times")
    print("--- End report ---")
    

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

def sort_on(dict):
    return dict["num"]

main()