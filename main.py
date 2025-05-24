import sys
from stats import count_words, count_letters, sort_char_dict


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    word_count = count_words(text)
    char_dict = count_letters(text)
    sorted_char_dict = sort_char_dict(char_dict)
    report(book, word_count, sorted_char_dict)


def get_book_text(book):
    with open(f"{book}") as f:
        return f.read()


def report(book, word_count, char_dict_sorted):
    print(f"Report for word count and letter count of {book}\n")
    print(f"Found {word_count} total words\n")
    for entry in char_dict_sorted:
        if entry['letter'].isalpha():
            print(f"{entry['letter']}: {entry['count']}")
    print(f"\nEnd of report for {book}")


main()
