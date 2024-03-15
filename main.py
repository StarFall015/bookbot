def main():
    text = get_book_text()
    count_words(text)


def get_book_text():
    with open("books/frankenstein.txt") as f:
        return f.read()


def count_words(file):
    words = file.split()
    print(len(words))


main()
