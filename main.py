def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sort_dict = get_sort_dict(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for char_data in sort_dict:
        print(f"The '{char_data['char']}' character was found {char_data['num']} times")

    print("--- End report ---")

    
def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def get_sort_dict(text):
    chars_dict = get_chars_dict(text)

    char_list = []
    for char, count in chars_dict.items():
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)
    return char_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()