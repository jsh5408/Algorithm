## 5525. IOIOI - python3
https://www.acmicpc.net/problem/5525

#### 내 풀이 - 50 점
```
from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
S = stdin.readline().strip()

ans = 0
P = "OI"*N

for i in range(M):
    if N*2 >= M:
        break
    if S[i] == "I":
        if S[i+1:i+1+N*2] == P:
            ans += 1

print(ans)
```
처음 I 를 제외한 OI 의 개수가 N 과 같다는 점을 이용

I 를 만나면 이후에 N 개의 OI 가 오는지 확인해서 ans + 1
for 문 + 슬라이싱 때문에 시간초과 돼서 50 점인 것 같다...

![](https://images.velog.io/images/jsh5408/post/5328bdfd-ac3f-40c4-989e-1fea14073c31/image.png)

#### 다른 사람의 풀이
```
from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
S = stdin.readline().strip()

ans = 0
count = 0
i = 1

while i < M - 1:
    if S[i-1] == "I" and S[i] == "O" and S[i+1] == "I":
        count += 1
        if count == N:
            count -= 1
            ans += 1
        i += 1
    else:
        count = 0
    i += 1

print(ans)
```
IOI 의 개수가 N 과 같다는 점을 이용

IOI 의 개수를 세서 N 개가 되면 ans + 1 해주는 단순한 방법

슬라이싱으로 안돼서 슬라이딩 윈도우도 생각해보고 했지만
내가 너무 어렵게 생각한듯...

![](https://images.velog.io/images/jsh5408/post/f69c13e5-a2c2-4ee7-bd28-e7dc39122a8e/image.png)