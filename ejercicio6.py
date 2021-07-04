def count_words(string):
    words = string.split(' ')
    words_dict = {}
    for word in words:
        words_dict.setdefault(word.lower(), 0)
        words_dict[word.lower()] += 1
    return words_dict


def most_common(word_dict):
    value = 0
    key = None
    for k, v in word_dict.items():
        if v > value:
            value = v
            key = k
    return key, value


my_dict = count_words('This is a sample sample sample words, this')
print(most_common(my_dict))
