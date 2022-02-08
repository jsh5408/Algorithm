## 1541. 잃어버린 괄호 - python3
https://www.acmicpc.net/problem/1541

#### 내 풀이 - 성공
```
inp = input().split("-")
ans = 0

first = inp.pop(0).split("+")
for n in first:
    ans += int(n)

for i in inp:
    tmp = 0
    nums = i.split("+")
    for n in nums:
        tmp += int(n)
    ans -= tmp

print(ans)
```
최솟값이 되려면 음수의 역할이 중요하니까 - 를 기준으로 split

맨 처음 값은 부호가 없으므로 ans 에 더해준다
=> + 들의 모임일 수도 있으니 + 를 기준으로 split 해서 ans 에 합함

나머지는 + 를 기준으로 split 한 후 합쳐서 빼주면 끝~

![](https://images.velog.io/images/jsh5408/post/57cff44d-e4d8-46cd-85ec-34c70cd93664/image.png)