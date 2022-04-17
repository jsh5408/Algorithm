## 17219. 비밀번호 찾기
https://www.acmicpc.net/problem/17219

#### Dictionary - 성공
```
from sys import stdin

N, M = map(int, stdin.readline().split())
dic = {}

for i in range(N):
    address, password = map(str, stdin.readline().split())
    dic[address] = password

for i in range(M):
    address = stdin.readline().strip()
    print(dic[address])
```

파이썬의 딕셔너리를 이용해 풀었다

> 이 때, **주의**해야할 점!
`stdin.readline()` 은 입력값의 개행문자까지 가져오기 때문에 `strip()` 이 필요하다
ex) 입력값: `acmicpc.net` / 실제 받아오는 값: `acmicpc.net\n`

![](https://velog.velcdn.com/images/jsh5408/post/6773f3ab-cd9b-4405-93e5-b12369bac096/image.png)
