## 1181. 단어 정렬 - python3
https://www.acmicpc.net/problem/1181

#### 내 풀이 - 성공
```
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
```
중복되지 않는 단어들만 `words` 에 저장하고 길이를 기준으로 정렬을 해준 후
`dic` 에 같은 길이의 단어들을 묶어서 저장

다시 `dic` 값을 보면서 `value` 값을 정렬하고 print

![](https://images.velog.io/images/jsh5408/post/f4e66491-0f9a-46f1-b42c-a6d70a3f26c6/image.png)

#### 내 풀이 2 - 성공
```
N = int(input())
words = []

for i in range(N):
    w = input()
    words.append((len(w), w))

words = list(set(words))

words.sort(key=lambda w: (w[0], w[1]))

for l, w in words:
    print(w)
```
(단어의 길이, 단어) 형태로 저장 후,
sort key 를 이용해서 한꺼번에 정렬

![](https://images.velog.io/images/jsh5408/post/6496ced3-32c9-4271-85c3-807ccd71ede9/image.png)