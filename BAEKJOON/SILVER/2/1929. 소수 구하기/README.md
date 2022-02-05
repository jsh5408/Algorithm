## 1929. 소수 구하기 - python3
https://www.acmicpc.net/problem/1929

#### 내 풀이 - 성공
```
M, N = map(int, input().split())
nums = [1]*(N+1)
nums[0], nums[1] = 0, 0

r = int(N**0.5)
for i in range(2, r+1):
    if nums[i]:
        for j in range(i+i, N+1, i):
            nums[j] = 0

for i in range(M, N+1):
    if nums[i]:
        print(i)
```
전에 봤던 에라토스테네스의 체를 이용해서 풀어봤다

큰 수인 N 만큼 nums 를 만들어서 1 로 초기화
2 ~ 루트N 까지의 숫자들의 배수를 모두 0 으로 바꿔주기
(0, 1 도 0 으로 바꿔줌)

nums 값이 1 인 숫자들이 소수이므로 M ~ N 까지의 숫자들을 보며 1 만 출력

![](https://images.velog.io/images/jsh5408/post/a5f584be-0b94-46be-8ec9-f595427342a8/image.png)