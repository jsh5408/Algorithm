## 1620. 나는야 포켓몬 마스터 이다솜 - python3
https://www.acmicpc.net/problem/1620

#### 내 풀이 - 성공
```
from sys import stdin

N, M = map(int, stdin.readline().split())
ans = [0] * (M)

nums = {}
names = {}
for i in range(N):
    inp = stdin.readline().strip()
    nums[i+1] = inp
    names[inp] = i+1

for i in range(M):
    Q = stdin.readline().strip()
    if Q.isdigit():
        print(nums[int(Q)])
    else:
        print(names[Q])
```
이름을 key 값으로 갖는 딕셔너리 nums 와
숫자를 key 값으로 갖는 딕셔너리 names 를 만들어서 저장

M 개의 입력을 받으며 숫자면 nums 의 값을 print
아니면 names 의 값을 print

이 문제는 문제 자체 난이도 보다도 **시간 초과** 해결이 관건이었다...

1. 하나의 dic 에 숫자, 이름 key 값 모두 저장해서 사용 -> 시간 초과
=> {"1": "Pikachu", "Pikachu": "1", ... }
2. nums, names 로 구분 -> 시간 초과
3. 그냥 리스트에 저장한 후 index 와 value 값 이용 -> 시간 초과
4. 바로 print 하지 않고 ans 에 저장해서 한번에 출력 -> 시간 초과
5. ans 에 저장할 때 append 대신 미리 크기 지정 -> 시간 초과
... 등등 별 방법 다 써봄

그러다 안되겠다 싶어서 사용한 건 input() 대신 stdin.readline() 사용

딕셔너리 & stdin.readline() & 바로바로 출력 을 이용하니까 통과됐다.

> **백준 Python3 속도 개선**
>
> 1. **input()** 보다 **stdin.readline()** 이 더 빠르다.
>
주의할 점, stdin.readline() 은 개행문자까지 같이 저장되므로 strip() 필요
숫자 입력이면 strip() 없이 int() 사용
그 외에 map() 사용 방식은 input() 과 동일
>
2. 리스트에 append 하지 말고 미리 크기 지정하기
>
>
3. 매 값마다 print() 하기보다는 하나의 string 에 개행문자와 함께 저장해서 한번에 출력
ex) s += a + '\n' & print(s)
>
참고) https://breakcoding.tistory.com/109

![](https://images.velog.io/images/jsh5408/post/2cbd125b-d012-4423-905b-9c5d5dd49203/image.png)
