## 1018. 체스판 다시 칠하기
https://www.acmicpc.net/problem/1018

#### 내 풀이 - 실패
```
### input
inp = input()
n, m = inp.split()
n = int(n)
m = int(m)

board = []

for i in range(n):
  b = input()
  tmp = []
  board.append(b)

ans = 64

for i in range(n-7):
  for j in range(m-7):
    if board[i][j] == "W":
      wb = 0
    else:
      wb = 1
    tmp = 0
    for r in range(8):
      for c in range(8):
        if (wb == 0 and board[i+r][j+c] == "B") or (wb == 1 and board[i+r][j+c] == "W"):
          tmp += 1
        if c != 7:
          wb = (wb + 1) % 2
    if ans > tmp:
      ans = tmp

print(ans)
```
`n`, `m`, `board` 모두 입력받고
`ans` 는 최댓값인 64 로 초기화

체스판의 시작 값은 `n-7 * m-7` 만 가능하니까
해당 크기만큼 보면서 `8 * 8` 만큼이 규칙에 맞는지 확인

`wb` 는 0 또는 1 로 번갈아가면서 계속 바뀌고
규칙에 맞지 않을 때마다 `tmp + 1`

`ans` 는 최솟값으로 update

근데... 안됐다...ㅎ
아마 처음 시작값을 고정해서 그런 듯

![](https://images.velog.io/images/jsh5408/post/32fb60b1-3733-4f16-9cf0-4096ff07dd0b/image.png)

#### 다른 사람의 풀이
```
N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        W = 0
        B = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        W += 1
                    if original[i][j] != 'B':
                        B += 1
                else:
                    if original[i][j] != 'B':
                        W += 1
                    if original[i][j] != 'W':
                        B += 1
        count.append(min(W, B))

print(min(count))
```
`W` : `W` 로 시작하는 경우
`B` : `B` 로 시작하는 경우

`(i+j)` 가 짝수면 시작 값과 같아야 하고 홀수면 달라야 함
각 경우마다 바꿔야하는 횟수를 더해주고
최솟값을 `count` 에 저장

모든 경우 중 최솟값 return

> 입력 방식 참고 - map() 이용
```
N, M = map(int, input().split())
original = []
count = []
>
for _ in range(N):
    original.append(input())
```

> 참고) https://god-gil.tistory.com/62

![](https://images.velog.io/images/jsh5408/post/9020b518-2899-4195-80fd-138dc6848b99/image.png)
