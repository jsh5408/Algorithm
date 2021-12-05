## 1085. 직사각형에서 탈출 - python3
https://www.acmicpc.net/problem/1085

#### 내 풀이 - 성공
```
x, y, w, h = map(int, input().split())

ans = min(x, y, w-x, h-y)

print(ans)
```
`(x, y)` 와 직사각형의 경계선까지의 경우는 총 4 가지이므로
그 중 최솟값을 찾아서 출력

![](https://images.velog.io/images/jsh5408/post/f109ee21-1815-4950-a679-1d759ceb161b/image.png)
