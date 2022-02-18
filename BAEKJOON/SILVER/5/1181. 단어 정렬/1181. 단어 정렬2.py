N = int(input())
words = []

for i in range(N):
    w = input()
    words.append((len(w), w))

words = list(set(words))

words.sort(key=lambda w: (w[0], w[1]))

for l, w in words:
    print(w)