## 1259. 팰린드롬수 - python3
https://www.acmicpc.net/problem/1259

#### 내 풀이 - 성공
```
while True:
    num = input()
    if num == "0":
        break
    yn = 1
    for i in range(len(num)//2):
        if num[i] != num[len(num)-i-1]:
            print("no")
            yn = 0
            break
    if yn:
        print("yes")
```
0 이 나올 때까지 입력을 계속 받아야 하므로 `while True`

반으로 잘라서 대칭이 되는지 확인
=> 대칭이면 yes 아니면 no 출력

![](https://images.velog.io/images/jsh5408/post/5b467f59-c572-4e0b-9eca-bcc6a7c7c786/image.png)
