## 소수 찾기 - Level 2
https://programmers.co.kr/learn/courses/30/lessons/42839

#### 내 풀이 - 통과
```
combinations = set()
def solution(numbers):
    global combinations
    def comb(nums, c):
        if c and int(c) > 1:
            combinations.add(int(c))
        
        if len(nums) == 0:
            return
        
        for i in range(len(nums)):
            comb(nums[:i] + nums[i+1:], c+nums[i])
    
    comb(numbers, "")
    
    answer = 0
    for c in combinations:
        isPrime = 1
        for i in range(2, int(c**0.5)+1):
            if c % i == 0:
                isPrime = 0
                break
        if isPrime:
            answer += 1
    
    return answer
```
종이 조각으로 만들 수 있는 모든 숫자의 경우를 `combinations` 에 저장
=> 재귀 함수 comb 를 이용

구한 숫자들은 소수인지 판단하기 위해 `2 ~ 루트 c` 까지 약수가 있는지 확인

소수들의 개수만 세줘서 return

![](https://images.velog.io/images/jsh5408/post/4dac1d7c-d152-447d-84e8-87b77a5fd2b0/image.png)

#### 다른 사람의 풀이
```
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
```
정말 천재같은 코드...

1) 숫자들의 조합 구하기
`a |= set(map(int, map("".join, permutations(list(n), i + 1))))`
- `permutations(list(n), i + 1))` => 리스트 `n` 을 이용한 `i+1` 길이의 조합
- 문자열로 합친 후 int 로 바꿔서 `a` 에 저장
- `|=` => 중복 제거

2) `a` 에서 `0 ~ 1` 값은 제거
(=> set 를 `-` 연산을 이용해서 제거 가능하다는 걸 첨 알았다,,)

3) 소수 찾기
범위: `2 ~ 루트 (최댓값)`
`a -= set(range(i * 2, max(a) + 1, i))`
- range 를 이용해서 `i` 의 배수들은 `a` 에서 모두 제거

> **에라토스테네스 체**
: `2 ~ 루트 n` 까지의 숫자들을 보면서 각 숫자들의 배수들을 미리 없애주는 방식
```
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n
>
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
>
    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
```
>
시간 복잡도: `O(N**0.5)`
>
https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4

![](https://images.velog.io/images/jsh5408/post/7902ebed-ca20-4621-93c7-4f1be93fd261/image.png)