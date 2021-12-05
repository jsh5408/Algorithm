## 2839. 설탕 배달 - python3
https://www.acmicpc.net/problem/2839

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())
nums = [-1]*(N+1)

if N == 3:
    print(1)
elif N == 4:
    print(-1)
else:
    nums[3] = 1
    nums[5] = 1

    for i in range(6, N+1):
        if nums[i-5] != -1:
            nums[i] = nums[5] + nums[i-5]
        elif nums[i-3] != -1:
            nums[i] = nums[3] + nums[i-3]
    print(nums[N])
```
nums 리스트를 만들어서 처음 3, 5 만 1 로 초기화

3, 4 일 경우는 예외 처리해주고
5 이상일 경우는 반복문 돌려서 dp 이용

5 를 뺀 값이 3 을 뺀 값 보단 작은 값이 될 것이므로
nums[i-5] 부터 확인하고 nums[i-3] 확인
둘 다 -1 이면 그대로 통과

N 번째 값 print

크게 어려운 문제가 아녔는데
N 이 3, 4, 5 일 때의 예외처리를 제대로 안해줘서 엄청 오래 걸렸다...ㅎ
**IndexError** => 항상 **범위 체크**를 잘 할 것!!!!

![](https://images.velog.io/images/jsh5408/post/faca373d-3a3f-4ec8-b739-ec7487a00d90/image.png)