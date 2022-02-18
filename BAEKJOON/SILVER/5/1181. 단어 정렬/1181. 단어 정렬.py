import collections

N = int(input())
words = []

for i in range(N):
    w = input()
    if w not in words:
        words.append(w)

words.sort(key=len)

dic = collections.defaultdict(list)

for w in words:
    dic[len(w)].append(w)

for k, v in dic.items():
    v.sort()
    for i in v:
        print(i)