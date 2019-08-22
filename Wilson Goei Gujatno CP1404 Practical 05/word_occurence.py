WORDS = {}

text = str(input("Text: ")).split()
counter = 0
for word in text:
    WORDS[word] = WORDS.get(word, 0) + 1
    sort_words = sorted(WORDS.items())

maximum_len = max(len(word) for word in WORDS)
for i in WORDS:
    print("{:{}} : {}".format(sort_words[counter][0],maximum_len,sort_words[counter][1]))
    counter += 1
