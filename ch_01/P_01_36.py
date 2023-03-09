# P-1.36 Write a Python program that inputs a list of words, separated by white-
# space, and outputs how many times each word appears in the list. You
# need not worry about efﬁciency at this point, however, as this topic is
# something that will be addressed later in this book.

def get_word_frequency(words: str) -> dict:
    word_list = words.split(" ")
    word_freq = {}
    for word in word_list:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


if __name__ == '__main__':
    words = input("Enter words separated by whitespace: ")
    word_frequency = get_word_frequency(words)
    print(word_frequency)
