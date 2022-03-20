## 구명보트
https://programmers.co.kr/learn/courses/30/lessons/42885

#### 내 풀이 - 통과
```
def solution(people, limit):
    answer = len(people)
    people.sort()
    idx = 0
    for i in range(len(people)-1, -1, -1):
        if people[i] == 0:
            continue
        for j in range(idx, i):
            if people[i] + people[j] <= limit:
                people[i] += people[j]
                people[j] = 0
                idx = j+1
            else:
                break
    zero = people.count(0)
    
    return answer - zero
```
구명보트의 최댓값 = 사람 수 이므로 `answer` 는 `len(people)` 로 초기화
사람은 몸무게 순으로 정렬해준다

무거운 사람부터 보면서 가벼운 사람 중에 같이 탈 수 있는 사람을 최대한 구함
=> `for i in range(len(people)-1, -1, -1):` & `for j in range(idx, i):`

동행자가 있을 경우, 가벼운 사람은 0 으로 바꿔주고 무거운 사람의 무게와 합쳐준다
`idx` 는 그 다음으로 가벼운 사람을 가리키도록 함

모두 합쳐줬으므로 무게가 있는 사람들의 수를 return

> 통과되긴 했지만 **"한 번에 최대 2명"** 이라는 조건을 못 봤다...ㅠ
최대 2 명이라면 2 중 for 문 사용해서 최대한의 인원을 합칠 필요 없이
그냥 하나의 반복문으로 가벼운 사람과 무거운 사람만 보면 될 듯!!

![](https://images.velog.io/images/jsh5408/post/558cab0b-cd21-41a5-9275-e399091113d8/image.png)

#### 다른 사람의 풀이
```
def solution(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
```
몸무게를 기준으로 정렬한 후,
제일 가벼운 사람 + 제일 무거운 사람을 묶어서 확인

동행자를 구한 사람들만 `answer` 로 세줘서 전체 인원에서 빼주기

![](https://images.velog.io/images/jsh5408/post/064fb5e6-f915-46b2-865c-73f185763267/image.png)

투 포인터를 사용해서 더 빠르다!!