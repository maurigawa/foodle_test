def sentence_word_count(sentence: str, n: int):
    words = sentence.split()
    word_count = []

    # Add word and count to word_count
    for word in words:
        if (word, words.count(word)) not in word_count:
            word_count.append((word, words.count(word)))

    # get the n most frequent words
    word_count = sorted(word_count, key= lambda x: x[0], reverse=False)
    word_count = sorted(word_count, key= lambda x: x[1], reverse=True)
    res = word_count[0:n]

    return res