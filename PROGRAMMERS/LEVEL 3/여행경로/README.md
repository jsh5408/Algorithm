## 여행경로
https://programmers.co.kr/learn/courses/30/lessons/43164

#### 내 풀이 - 통과
```
def func(dic, now, path, length):
    if length == 0:
        return [path]
    
    if len(dic[now]) == 0:
        return []
    
    ans = []
    for i in range(len(dic[now])):
        p = dic[now].pop(0)
        ans += func(dic, p, path+[p], length-1)
        dic[now].append(p)
    return ans

def solution(tickets):
    answer = []
    dic = {}
    
    for a, b in tickets:
        if a in dic:
            dic[a].append(b)
        else:
            dic[a] = [b]
        if b not in dic:
            dic[b] = []
    
    answer = func(dic, "ICN", ["ICN"], len(tickets))
    answer.sort()
    
    return answer[0]
```
`dic` 에 출발지를 기준으로 도착지들 모두 저장

재귀의 시작은 `ICN` 부터
지금 출발지와 연결된 도착지는 다음 재귀로 넘길 때 제거 하고 넘김
=> pop & append

모든 항공권을 사용해야 하므로 `len(tickets)-1` 로 0 이 되는지 확인

모든 경로들은 `answer` 에 저장해서
알파벳 순으로 정렬 후 가장 첫번째 값 return

마지막에 정렬하지 않고
`dic` 에 저장된 값들을 정렬해준 후, 재귀 돌려도 가능

![](https://images.velog.io/images/jsh5408/post/4c187666-093b-4ad8-9cd2-da2202c4e7b8/image.png)