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


print(text_to_string(main()))

