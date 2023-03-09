def reverse_words(sentence: str) -> str:
    words_list = sentence.split(" ")
    reverse_words_list = []

    for word in words_list:
        reverse_word = ""
        for index in range(len(word) - 1, -1, -1):
            reverse_word += word[index]

        reverse_words_list.append(reverse_word)
    return " ".join(reverse_words_list)


reverse = reverse_words("Hello world")
print(reverse)  # Output: "olleH dlrow"
