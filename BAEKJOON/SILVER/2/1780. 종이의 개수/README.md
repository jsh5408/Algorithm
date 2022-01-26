## 1780. 종이의 개수 - python3
https://www.acmicpc.net/problem/1780

#### 내 풀이 - 실패
```
from sys import stdin
import collections

N = int(stdin.readline())
paper = []
for i in range(N):
    p = list(map(int, stdin.readline().split()))
    paper.append(p)

ans = [0]*3

papers = collections.deque([paper])
while papers:
    p = papers.popleft()
    
    # 종이 p 가 몇가지의 숫자로 이루어져있는지 확인
    nums = []
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] not in nums:
                nums.append(p[i][j])
        if len(nums) > 1:
            break
            
    l = len(p)
    a = l//3
    # 여러개의 숫자로 이루어져있는 경우 9 등분
    if len(nums) > 1 and a > 1:
        for i in range(0, l, a):
            for j in range(0, l, a):
                paper = []
                for k in range(3):
                    paper.append(p[j+k][i:i+a])
                if len(paper) > 0:
                    papers.append(paper)
    # 종이의 크기가 3*3 인 경우 => 숫자 하나하나가 종이이므로 세줌
    elif len(nums) > 1 and a == 1:
        for i in range(len(p)):
            for j in range(len(p[i])):
                ans[p[i][j]+1] += 1
    # 종이가 하나의 숫자로 이루어진 경우 ans + 1
    else:
        ans[nums[0]+1] += 1

print(ans)
```
papers 에 확인해야하는 종이들을 모두 저장해서
하나씩 pop 해가면서 같은 숫자로 이루어졌는지 확인

다른 숫자로 이루어져있다면 9 등분 해서 각 종이마다 papers 에 저장
같은 숫자로 이루어져있다면 해당 값 + 1

#### 다른 사람의 풀이
```
import sys
input = sys.stdin.readline

n = int(input())
minus_cnt, zero_cnt, plus_cnt = 0, 0, 0

papers = []
for _ in range(n):
    row = list(map(int, input().rsplit()))
    papers.append(row)

def check(row, col, n):
    global minus_cnt, zero_cnt, plus_cnt
    curr = papers[row][col]

    for i in range(row, row + n):
        for j in range(col, col + n):
            if papers[i][j] != curr:
                next_n = n // 3
                check(row, col, next_n)  # 1
                check(row, col + next_n, next_n)  # 2
                check(row, col + (2 * next_n), next_n)  # 3
                check(row + next_n, col, next_n)  # 4
                check(row + next_n, col + next_n, next_n)  # 5
                check(row + next_n, col + (2 * next_n), next_n)  # 6
                check(row + (2 * next_n), col, next_n)  # 7
                check(row + (2 * next_n), col + next_n, next_n)  # 8
                check(row + (2 * next_n), col + (2 * next_n), next_n)  # 9
                return

    if curr == -1:
        minus_cnt += 1
    elif curr == 0:
        zero_cnt += 1
    elif curr == 1:
        plus_cnt += 1
    return

check(0, 0, n)

print(minus_cnt)
print(zero_cnt)
print(plus_cnt)
```
분할정복 이용 => 재귀함수 check()

주어진 `papers[row][col]` 와 다른 값이 하나라도 존재하면 9 등분
현재 종이가 모두 같은 값이라면 해당 cnt + 1

분할정복 연습하기!!!

![](https://images.velog.io/images/jsh5408/post/d2e1a42c-2f52-495e-bed1-f95c9cc90362/image.png)