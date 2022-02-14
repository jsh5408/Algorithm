## 1654. 랜선 자르기 - python3
https://www.acmicpc.net/problem/1654

#### 내 풀이 - 시간 초과
```
K, N = map(int, input().split())
lines = []
ans = 0

for _ in range(K):
    lines.append(int(input()))

for length in range(1, max(lines)):
    cnt = 0
    for l in lines:
        cnt += l // length
    if cnt >= N:
        ans = max(ans, length)
    else:
        break

print(ans)
```
기존 랜선의 최대 길이까지 넉넉하게 범위를 잡아준 후
length 만큼 랜선 자르기 진행

cnt 가 N 개 이상이면 ans 를 최대 길이로 update
N 개 이하가 되면 바로 break

너무 오래 걸려서 시간 초과가 된다...

![](https://images.velog.io/images/jsh5408/post/be54f905-c692-4810-af26-6359cfb4dabf/image.png)

#### 내 풀이 2 - 성공
```
K, N = map(int, input().split())
lines = []
ans = 0

for _ in range(K):
    lines.append(int(input()))

left = 1
right = max(lines)

while left <= right:
    mid = (left+right) // 2

    cnt = 0
    for l in lines:
        cnt += l // mid
    if cnt >= N:
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)
```
알고리즘 분류에서 힌트를 얻고 이분탐색으로 풀었다...!

left = 1, right = 최대 길이의 랜선
mid 값으로 랜선 자르기를 진행한 후
N 보다 크거나 같으면 ans update & left 를 이동해서 mid 값 키워주기
N 보다 작으면 right 를 이동해서 mid 값 줄여주기

> `left <= right` or `left < right` 의 차이를 아직 잘 모르겠다...

![](https://images.velog.io/images/jsh5408/post/b73657c0-c48f-45ed-ba8c-8258c8083835/image.png)