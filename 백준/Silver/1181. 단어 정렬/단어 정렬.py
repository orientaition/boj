words= int(input())
word_li = []
for _ in range(words):
    word = str(input())
    word_c = len(word)
    word_li.append((word, word_c))
word_li = list(set(word_li))
word_li.sort(key = lambda word: (word[1], word[0]))
for word in word_li:
    print(word[0])