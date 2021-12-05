## 1074. Z - python3
https://www.acmicpc.net/problem/1074

#### 내 풀이 - 실패
```
N, r, c = map(int, input().split())

w = 2 ** N
size = w * w
block = size // 8

ans = 0

if r % 2 == 0 and c % 2 == 0:
    ans += 0
elif r % 2 == 0 and c % 2 != 0:
    ans += 1
elif r % 2 != 0 and c % 2 == 0:
    ans += 2
elif r % 2 != 0 and c % 2 != 0:
    ans += 3

...

print(ans)
```
`(r, c)` 좌표가 어떤 블럭에 위치해 있는지 파악해서

(짝수, 짝수) => 0 번째
(짝수, 홀수) => 1 번째
(홀수, 짝수) => 2 번째
(홀수, 홀수) => 3 번째

라는 점을 이용하려 했는데...
`N` 이 커질수록 어떻게 처리해야할지 모르겠음...

![](https://images.velog.io/images/jsh5408/post/f649d092-7602-4d24-a7d7-930ef84625b8/image.png)

고뇌의 흔적..^^


#### 다른 사람의 풀이
```
N, r, c = map(int, input().split())
cnt = 0

while N > 1:
    size = (2 ** N) // 2
    if r < size and c < size: # 2사분면
        pass
    elif r < size and c >= size: # 1사분면
        cnt += size ** 2
        c -= size
    elif r >= size and c < size: # 3사분면
        cnt += size ** 2 * 2
        r -= size
    elif r >= size and c >= size: # 4사분면
        cnt += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)
```
전체 `size`를 기준으로 계속해서 4 개의 사분면으로 나누기

Z 는 2 -> 1 -> 3 -> 4 사분면 순으로 이동

2 사분면 => 유지
1 사분면 => 열만 `2 ** N` 만큼 감소
3 사분면 => 행만 `2 ** N` 만큼 감소
4 사분면 => 행 열 모두 `2 ** N` 만큼 감소

> 참고) https://velog.io/@jajubal/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EB%B0%B1%EC%A4%80-1074-Z

![](https://images.velog.io/images/jsh5408/post/86cd13ff-84f2-4c95-9cf6-9e60b8b87a4d/image.png)
