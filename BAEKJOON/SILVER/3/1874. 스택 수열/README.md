## 1874. 스택 수열 - python3
https://www.acmicpc.net/problem/1874

#### 내 풀이 - 성공
```
n = int(input())
stack = [1]
inp = []
out = []
result = ["+"]

for _ in range(n):
    inp.append(int(input()))

i = 2
while inp:
    if len(stack) == 0 or inp[0] > stack[-1]:
        result.append("+")
        stack.append(i)
        i += 1
    elif inp[0] == stack[-1]:
        inp.pop(0)
        result.append("-")
        stack.pop()
    else:
        if inp[0] in out:
            break
        while stack and inp[0] != stack[-1]:
            result.append("-")
            out.append(stack.pop())

if len(inp) > 0:
    print("NO")
else:
    for r in result:
        print(r)
```
stack 은 1 부터 시작하므로 미리 1 을 넣어주고 result 도 "+" 부터 넣어줌

다음으로 stack 에 들어갈 값은 i => 2 로 초기화

inp[0] 값과 같아질 때까지 i 를 stack 에 저장 & i+1
같아지면 pop & "-"

그 외에 지금 원하는 값이 stack[-1] 보다 작으면 => stack 안에 있거나 이미 pop 된 값
이미 pop 된 값이면 수열이 만들어질 수 없으므로 break 후 "NO" 출력
stack 안에 있는 값이면 계속 pop 해가기

통과는 됐지만 메모리와 시간이 안타깝다...

![](https://images.velog.io/images/jsh5408/post/c3fd73e5-9630-42dc-91e8-77a611461756/image.png)

#### 다른 사람의 풀이
```
n = int(input())
stack = []
result = []
flag = 0
cur = 1

for i in range(n):
    num = int(input())
    
    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        flag = 1
        break               

if flag == 0:
    for r in result:
        print(r)
```
stack 과 result 만 사용

숫자들을 미리 다 받지 않고 input 받으면서 그때그때 확인

cur 는 현재 어디까지 숫자가 사용됐는지를 나타냄
num 보다 작으면 같을 때까지 push, 같아지면 pop
같지 않다면 오름차순이 불가능하다는 것이므로 "NO" & break

내가 풀 때는 **1 ~ N 의 숫자들이 모두 입력된다**는 것을 간과해서 복잡하게 푼 거 같다...
=> stack 의 top 이 input 보다 크면 버려지는 숫자가 생김

![](https://images.velog.io/images/jsh5408/post/762d5ba1-e04b-40c1-9b53-53706e1360c0/image.png)