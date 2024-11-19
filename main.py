def main():
                                
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents


def text_to_string(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count


def letter_count(string):
    letters = {}
    for each in string:
        lower_word = each.lower()
        if lower_word in letters:
            letters[lower_word] += 1
        else:
            letters[lower_word] = 1
    return letters


def sort_on(dict):
    return dict["num"]


def book_report(text):
    word_count = text_to_string(text)
    char_count = letter_count(text)
    char_list = []
    for char, num in char_count.items():
        if char.isalpha():
            char_dict = {"char": char, "num": num}
            char_list.append(char_dict)

    char_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char in char_list:
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    
    print("--- End report ---")


book_report(main())

