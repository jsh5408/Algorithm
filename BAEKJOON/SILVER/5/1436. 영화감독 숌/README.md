## 1436. 영화감독 숌 - python3
https://www.acmicpc.net/problem/1436

#### 내 풀이 - 실패
```
N = int(input())

end = "666"

print(int(str(N-1)+end))
```
666, 1666, 2666, 3666, ... 의 순서라면
**(N-1) 666** 의 형태를 갖는다고 생각함

근데.. 아니었다...
5666 다음에는 6666 이 아니라 **6660** 이 됨
=> ..., 5666, 6660, 6661, 6662, 6663, 6664, ...

#### 다른 사람의 풀이
```
n = int(input())
x = 666

while n:
    if '666' in str(x):
        n -= 1
    x += 1

print(x - 1)
```
666 부터 시작해서 **666** 이 포함된 숫자일 때만 시리즈 제목으로 사용 => n - 1
나머지는 666 이 포함될 때까지 1 씩 증가

허무하다...

![](https://images.velog.io/images/jsh5408/post/ccb5f508-fe00-46d8-b388-ac2edfc39dd1/image.png)