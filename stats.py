def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    counts = {}

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts

def sort_character_counts(char_counts):
    sorted_char_counts = []

    for char in char_counts:
        char_dict = {"char": char, "num": char_counts[char]}
        sorted_char_counts.append(char_dict)

    sorted_char_counts.sort(reverse=True, key=sort_on)

    return sorted_char_counts

def sort_on(char_counts):
    return char_counts["num"]
    