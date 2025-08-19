from stats import get_num_words, count_characters, sort_character_counts

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(text)
    char_counts = count_characters(text)
    sorted_char_counts = sort_character_counts(char_counts)
    print_report(num_words, sorted_char_counts)

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()
    
def print_report(num_words, sorted_char_counts):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")

    for line in sorted_char_counts:
        if line["char"].isalpha():
            print(f"{line["char"]}: {line["num"]}")

    print("============= END ===============")
    
main()