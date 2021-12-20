## 15649. N과 M (1) - python3
https://www.acmicpc.net/problem/15649

#### 내 풀이 - 성공
```
from sys import stdin

N, M = map(int, stdin.readline().split())
nums = [i for i in range(1, N+1)]

def func(n, comb):
    if len(comb) == M:
        for c in comb:
            print(c, end=' ')
        print()
        return
    
    for i in range(len(n)):
        func(n[:i]+n[i+1:], comb+[n[i]])

func(nums, [])
```
1 ~ N 까지의 숫자들을 nums 에 저장

재귀를 돌려서 현재 n 리스트에 있는 숫자들을 하나씩 comb 에 추가
이때 해당 숫자를 제외한 나머지 숫자들은 합쳐서 다음 n 으로 보내기

그러다 comb 의 길이가 M 과 같아지면 출력

![](https://images.velog.io/images/jsh5408/post/d9569f9d-5cd6-4008-a85f-6e8123a614ab/image.png)