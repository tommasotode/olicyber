with open('camp/youcompleteme/words.txt') as f:
    words = list(sorted([word.strip().encode('utf-8') for word in f.readlines()]))

for w in words:
    if len(w) == 13 and w[-8] == w[-9] and w[-6] == w[-10] and w[-10] == w[-2]:
        print(w)