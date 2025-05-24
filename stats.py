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
