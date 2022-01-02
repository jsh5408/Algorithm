## 2609. 최대공약수와 최소공배수 - python3
https://www.acmicpc.net/problem/2609

#### 내 풀이 - 성공
```
from sys import stdin

A, B = map(int, stdin.readline().split())

a = set()
b = set()

for i in range(1, A+1):
    if A % i == 0:
        a.add(i)
    
for i in range(1, B+1):
    if B % i == 0:
        b.add(i)

gcd = a & b

print(max(gcd))
print((A*B)//max(gcd))
```
A, B 의 약수들을 각각 a, b 에 저장하고
최대공약수를 구하기 위해 a 와 b 의 교집합 a & b 인 gcd 를 구함

최대공약수는 gcd 의 최댓값
최소공배수는 `A*B` 를 최대공약수로 나눈 값이라는 것을 이용

![](https://images.velog.io/images/jsh5408/post/270356fe-8ec3-44f5-8f4e-7d30aa22679a/image.png)

#### 다른 사람의 풀이
```
from sys import stdin

A, B = map(int, stdin.readline().split())

# 최대공약수
def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

# 최소공배수
def LCM(a, b):
    result = (a*b) // GCD(a, b)
    return result

print(GCD(A, B))
print(LCM(A, B))
```
[유클리드 호제법](https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95)
호제법 = 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘

최대공약수)
**a, b 에 대해서 a 를 b 로 나눈 나머지를 r 이라 하면 (단, a>b),
a 와 b 의 최대공약수는 b 와 r 의 최대공약수와 같다**는 점을 이용

최소공배수)
`a*b` 를 최대공약수로 나눈 값

외워두자!!!

![](https://images.velog.io/images/jsh5408/post/e1830ec2-704f-472d-8090-1dbd1911c28b/image.png)