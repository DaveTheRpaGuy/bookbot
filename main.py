import sys

from stats import count_words, count_chars, sort_chars

#test: python3 main.py books/frankenstein.txt
#test: python3 main.py books/mobydick.txt
#test: python3 main.py books/prideandprejudice.txt
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.y <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)

    word_count = count_words(file_contents)
    char_counts = sort_chars(count_chars(file_contents))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    #print(char_counts)
    for char_count in char_counts:
        print(f"{char_count["char"]}: {char_count["num"]}")
    print("============= END ===============")

    #for char_count in char_counts_dict_list:
        #print(f"The '{char_count["char"]}' character was found {char_count["num"]} times")
    #print("--- End report ---")

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents



main()