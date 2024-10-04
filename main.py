def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lowered_text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def char_dict(text):
    text = text.lower()
    char_count = character_count(text)
    char_alpha = []
    for char, count in char_count.items():
        if char.isalpha():
            char_alpha.append((char, count))
    char_alpha.sort(reverse=True, key=lambda item: item[1])
    return char_alpha

def print_char_counts(char_alpha):
   for char, count in char_alpha:
        print(f"The {char} character appears {count} times.")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    char_count = character_count(text)
    char_alpha = char_dict(text)
    print(text)
    print(f"The text contains {word_count(text)} words.")
    print(f"The text contains the following characters {char_count}")
    print_char_counts(char_alpha)
    print("-- END OF REPORT --")
main()