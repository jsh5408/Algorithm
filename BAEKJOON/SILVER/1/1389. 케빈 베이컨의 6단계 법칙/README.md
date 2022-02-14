## 1389. 케빈 베이컨의 6단계 법칙 - python3
https://www.acmicpc.net/problem/1389

#### 내 풀이 - 성공
```
N, M = map(int, input().split())

graph = {i:[] for i in range(1, N+1)}
person = {i:[0]*(N+1) for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    person[a][b] = 1
    person[b][a] = 1

def func(p, target, cnt, visited):
    if person[p][target] > 0:
        return cnt + person[p][target]

    if p == target:
        return cnt
    
    ans = N
    for i in graph[p]:
        if i not in visited:
            ans = min(ans, func(i, target, cnt+1, visited+[p]))
    return ans

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if person[i][j] == 0:
            cnt = func(i, j, 0, [])
            person[i][j] = cnt
            person[j][i] = cnt


sums = []
for i in range(1, N+1):
    sums.append(sum(person[i]))
    
m = min(sums)
for i in range(len(sums)):
    if m == sums[i]:
        print(i+1)
        break
```
graph : 사람들 간의 연결 관계
person : 사람들 간의 몇단계 걸리는지 => 합이 케빈 베이컨의 수가 됨

입력 값으로 주어지는 연결들은 1 단계 이므로 person 값 = 1

그 이상의 단계는 재귀함수로 찾아줌
graph 로 연결된 사람들을 보면서 몇단계를 거치는지 확인
이미 구한 적 있는 연결 관계는 해당 값을 가져와 사용
양방향이므로 person[i][j] & person[j][i] 모두 update

모든 연결들이 구해지면 각 사람별 케빈 베이컨 수 구하기 => sums
최솟값을 찾은 후 가장 먼저 해당되는 값 return
=> 여러 명일 경우에는 번호가 가장 작은 사람을 출력이므로

![](https://images.velog.io/images/jsh5408/post/942d124e-0b07-4fad-b54e-4f5dd8d3b2c3/image.png)