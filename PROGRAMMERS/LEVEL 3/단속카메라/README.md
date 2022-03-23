## 단속카메라
https://programmers.co.kr/learn/courses/30/lessons/42884

#### 내 풀이 - 실패
```
def solution(routes):
    answer = len(routes)
    
    ### 모든 지점마다 dic 값 생성 ###
    dic = {}
    for s, e in routes:
        dic[s] = set()
        dic[e] = set()
        
    ### points: 지점들만 저장 ###
    points = list(dic.keys())
    points.sort()
    
    ### 각 지점마다 찍히는 자동차들 저장 ###
    for i in range(len(routes)):
        l = points.index(routes[i][0])
        r = points.index(routes[i][1])
        for j in range(l, r+1):
            dic[points[j]].add(i)
    
    ### 카메라에 찍힌 자동차들에 대한 정보 이용 ###
    cars = {i for i in range(len(routes))}
    
    ...
    
    return answer
```
```
예시
{-20: {0}, 15: {0}, -14: {0, 1, 2}, -5: {0, 1, 3}, -18: {0, 2}, -13: {0, 1, 2}, -3: {0, 3}}
```
각 포인트마다 카메라에 찍히는 자동차들을 저장해서 최소한의 횟수를 찾으려 함
but 횟수 찾는 부분을 구현하지 못했다...

#### 다른 사람의 풀이
```
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30001

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
```
`routes` 를 진출 지점을 기준으로 정렬

진입 지점의 값이 `-30000` 으로 정해져 있으므로 `last_camera = -30001`

`last_camera` 가 진입 지점 보다 작을 경우
=> 카메라에 찍히지 않는 범위 이므로 `answer + 1` & `last_camera` update

외우자!!!

![](https://images.velog.io/images/jsh5408/post/0266b06c-1e38-4e6b-84fd-0277b183c9ef/image.png)