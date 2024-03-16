def main():
    book = "frankenstein"
    text = get_book_text(book)
    word_count = count_words(text)
    char_dict = count_letters(text)
    sorted_char_dict = sort_char_dict(char_dict)
    report(book, word_count, sorted_char_dict)


def get_book_text(book):
    with open(f"books/{book}.txt") as f:
        return f.read()


def count_words(file):
    words = file.split()
    return (len(words))


def count_letters(text):
    char_dict = {}
    lower_text = text.lower().split()
    for word in lower_text:
        for letter in word:
            if (letter not in char_dict) and (letter.isalpha()):
                char_dict[letter] = 1
            elif letter in char_dict:
                char_dict[letter] += 1
    return char_dict


def sort_on(dict):
    return dict["count"]


def sort_char_dict(dict):
    sorted_dict_list = []
    for char in dict:
        temp_dict = {"letter": char, "count": dict[char]}
        sorted_dict_list.append(temp_dict)
    sorted_dict_list.sort(reverse=True, key=sort_on)
    return sorted_dict_list


def report(book, word_count, char_dict_sorted):
    print(f"Report for word count and letter count of {book}\n")
    print(f"{word_count} words were found in this book\n")
    for entry in char_dict_sorted:
        print(f"The letter {entry['letter']} was found {entry['count']} times")
    print(f"\nEnd of report for {book}")


main()
