def main():
    text = get_book_text("frankenstein")
    count_words(text)


def get_book_text(book):
    with open(f"books/{book}.txt") as f:
        return f.read()


def count_words(file):
    words = file.split()
    print(len(words))


def count_letters():



main()
