## 1966. 프린터 큐 - python3
https://www.acmicpc.net/problem/1966

#### 내 풀이 - 성공
```
from sys import stdin

T = int(stdin.readline())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    q = list(map(int, stdin.readline().split()))
    nums = [i for i in range(N)]
    i = 0
    while i < N:
        if i+1 < N and q[i] < max(q[i+1:]):
            q.append(q.pop(i))
            nums.append(nums.pop(i))
        else:
            i += 1
            
    print(nums.index(M)+1)
```
(우선순위, 인덱스) 형태로 저장하고
min-heap, deque, ... 써봤는데 잘 안됐다...ㅎ

그래서 그냥 우선순위가 담긴 리스트 q 와 문서의 번호를 담은 nums 두개의 리스트를 사용
문서의 순서가 바뀔 때마다 q 와 nums 동시에 변경하도록 함

우선순위 값을 하나씩 보면서 자신 이후에 큰 값이 존재하면
q 와 nums 모두 pop 한 후 맨 뒤에 다시 append

큰 값이 없다면 다음 값 확인하러 넘어감 => i += 1

nums 에서 `M 의 위치 + 1` 을 print 해주면 된다

* `max(q[i+1:])` 에서 slicing 하지 않고
그냥 max(q) 로 하고 q[i] 와 같으면 아예 pop 만 해서 제거해도 됐을 듯

![](https://images.velog.io/images/jsh5408/post/a7e3ea9a-89fd-42c4-974c-25706f69aeff/image.png)