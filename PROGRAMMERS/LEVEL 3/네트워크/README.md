## 네트워크
https://programmers.co.kr/learn/courses/30/lessons/43162

#### 내 풀이 - 통과
```
visited = []

def func(dic, com, net):
    global visited
    
    if visited[com]:
        return
    
    visited[com] = 1
    
    for i in range(len(net)):
        if visited[net[i]] == 0:
            func(dic, net[i], dic[net[i]])

def solution(n, computers):
    global visited
    answer = 0
    
    visited = [0] * n
    dic = {i:[] for i in range(n)}
    
    for i in range(len(computers)):
        for j in range(i+1, len(computers[i])):
            if i != j and computers[i][j]:
                dic[i].append(j)
                dic[j].append(i)
    
    for i in range(n):
        if visited[i] == 0:
            func(dic, i, dic[i])
            answer += 1
    
    return answer
```
우선 `dic` 에 각 컴퓨터마다 연결되는 컴퓨터들 저장
`0 ~ n-1` 까지의 각 컴퓨터마다 재귀로 연결된 네트워크를 세줌

이 때, 이미 하나의 네트워크에 연결된 컴퓨터들은 `visited` 값을 1 로 설정

![](https://images.velog.io/images/jsh5408/post/83e4557d-f305-4ee3-8877-49dd14ab1cc0/image.png)