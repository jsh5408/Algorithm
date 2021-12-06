## 11729. 하노이 탑 이동 순서 - python3
https://www.acmicpc.net/problem/11729

#### 다른 사람의 풀이
```
from sys import stdin

N = int(stdin.readline())

def hanoi(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi(n-1, start, 6-start-end)	# 1
    print(start, end)			# 2
    hanoi(n-1, 6-start-end, end)	# 3

print(2**N - 1)
hanoi(N, 1, 3)
```
**마지막 N 번째 원판이 3 번째 기둥으로 가려면 N-1 개의 원판들은 2 번째에 있어야 한다**
는 점을 이용

따라서
1. start 기둥에 있는 N-1 개의 원판들을 보조 기둥으로 모두 이동
2. N 번째 원판을 start -> end 로 이동
3. 보조 기둥에 있는 N-1 개의 원판들을 end 기둥으로 모두 이동

의 절차를 수행하면 된다.

6-start-end : 1, 2, 3 중 사용하지 않은 한가지의 탑을 찾아줌

![](https://images.velog.io/images/jsh5408/post/5ee98240-5f4d-4ac2-ac6b-2915aa0211da/image.png)