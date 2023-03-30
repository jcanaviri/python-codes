"""
Oneline cloud reading application similar to amazon kindle
(for short stories)

We need helpt designing actual application
(code that implements this)
A few things looking for:
* User have a library of books that they can add to or remove from.
* Users can set a book from theirs library as active.
* The reading application remembers where a user left off in a given book.
* The reading application only displays a page of text at a time in the active book.

** Remember
* All books in library
* Remember active book
* Remember last pages in all books
* Display a page in active book

** Classes:
* representing a book (Book)
    * id: str/int/uuid
    * title
    * pages/content in the book: list of string (per page)
    * last page user looked at: int (remember off-by-one)
* representing a library
    * collection of books: {id: Book()}
    * active book: string (some book id)
"""


# Desinging class part
class Book:
    def __init__(self, id, title, content) -> None:
        self.id = id
        self.title = title
        self.content = content
        self.last_page = 0

        self.font_size = 12
        # TODO: Implement the algorith for calculate how many characters
        # a page could have
        # self.charts_per_page = calculate(self.font_size)

    def display_page(self):
        start_idx = self.chars_per_page * self.last_page
        end_idx = start_idx + self.chars_per_page

        return self.content[start_idx:end_idx]

    def turn_page(self):
        self.last_page += 1
        return self.display_page()


class Library:
    def __init__(self) -> None:
        self.collection = dict()
        self.active_book = None
        self.counter_id = 0

    def add_to_collection(self, title, content):
        new_book = Book(self.counter_id, title, content)
        self.collection[new_book.counter_id] = new_book
        self.counter_id += 1

    def remove_from_collection(self, id):
        del self.collection[id]

    def set_active_book(self, id):
        self.active_book = id

    def display_page(self):
        return self.collection[self.active_book].display_page()

    def turn_page(self):
        return self.collection[self.active_book].turn_page()


"""
Avoid plagarism
* Detect two most likely books that might have plagiarism:
    longest shared common section of text

`I have this book I like to read`
`She has this book I like to watch`
"""


def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs = str1[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs


sentence_a = "I have this book I like to read"
sentence_b = "She has this book I like to watch"

print(longest_common_subsequence(sentence_a, sentence_b))
