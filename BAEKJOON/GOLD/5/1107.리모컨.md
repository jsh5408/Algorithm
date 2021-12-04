## 1107. 리모컨
https://www.acmicpc.net/problem/1107

#### 내 풀이 - 실패
```
N = input()
M = int(input())
inp = input().split()

# 채널 변경이 필요 없거나 불가능한 경우
if N == "100" or M == 10:
    print(0)
else:
    # nums => 모든 버튼별 시작 버튼을 저장
    nums = {str(i): i for i in range(10)}
    # unable => 고장난 버튼들
    unable = []
    for i in range(M):
        unable.append(inp[i])

    for k, v in nums.items():
        # 고장난 버튼들은 +- 를 최소로 하는 다른 버튼으로 시작값 변경
        if k in unable:
            K = int(k)
            # 이전 값과 이후의 값 중 최소 차이를 갖는 버튼 찾기
            n = nums[str(K-1)] if K != 0 else -10
            dif = K-n
            for i in range(K+1, 10):
                if str(i) not in unable:
                    if dif > i-K:
                        dif = i-K
                        n = i
                    break
            nums[k] = n

    ans = abs(int(N) - 100)	# 100 번부터 +- 이용하는 경우
    tmp = 0    # 새로 누르는 경우
    carry = 1
    
    # 목표 채널의 일의 자리부터 채널 변경 횟수 세주기
    if len(N) < 6:
        for i in range(len(N)-1, -1, -1):
            K = int(N[i])
            tmp += abs(K - nums[N[i]]) * carry + 1
            carry *= 10
    # 최대 500,000 번의 채널인 경우 고려
    else:
        i = len(N)-1
        for _ in range(5):
            K = int(N[i])
            tmp += abs(K - nums[N[i]]) * carry + 1
            carry *= 10
            i -= 1
        if nums[N[i]] > 5:
            tmp = ans
        else:
            tmp += 1

    ans = min(ans, tmp)

    print(ans)
```
`0 ~ 9` 각 버튼마다 시작 버튼값을 찾아줌

ex) `N = 5457` `M = 3` `unable = 6 7 8` => `result = 6`
0, 1, 2, 3, 4, 5, 9 => 각자 값으로 시작 => 1 의 값만 가짐
6 => 5 로 시작 => 자기 자신 + `-` 1 번 => 2 의 값을 가짐
7 => 5 로 시작 => 자기 자신 + `-` 2 번 => 3 의 값을 가짐
8 => 9 로 시작 => 자기 자신 + `+` 1 번 => 2 의 값을 가짐
==> `5457` = 1+1+1+3 = `6`

`nums` 가 `0 ~ 9` 까지 순차적으로 생성됐으므로
`for k, v in nums.items():` 에서도 순차적으로 `nums` 값을 update 한다고 봄

따라서 고장난 버튼은
**이전 값 + 1** 과 **이후 값 중에 사용 가능한 버튼을 찾는 것**
두가지 경우 중 최솟값으로 update 해줌

그러고 `N` 의 일의 자리부터 역순으로 채널 변경 횟수 세주기
각 버튼 별 시작 버튼과의 차이(+- 횟수) * 자릿수 를 더해주기

이때, 최대 채널은 500,000 인 점을 고려

그러나.. 테스트케이스들은 모두 통과하지만 fail...
코드 완성하면서도 뭔가 찝찝함이 남아있었다...ㅠ

![](https://images.velog.io/images/jsh5408/post/864b62a7-3abb-4711-b86a-285585ed860c/image.png)

#### 다른 사람의 풀이
```
N = int(input())
M = int(input())
enable = {str(i) for i in range(10)}

# 고장난 버튼 제거
if M != 0:
    enable -= set(map(str, input().split()))

ans = abs(100 - N)

for n in range(1000001):
    n = str(n)
    for j in range(len(n)):
        if n[j] not in enable:
            break
        elif j == len(n) - 1:
            ans = min(ans, abs(N - int(n)) + len(str(n)))
print(ans)
```
브루트 포스

사용 가능한 버튼들을 `enable` 에 저장

최대 500,000 번 채널이므로 최대 6 자리까지 확인 가능
=> 7 자리의 숫자 중 가장 작은 **1,000,000** 까지의 숫자들을 모두 확인

해당 숫자에 고장난 번호가 없으면 최소 횟수로 `ans` update

> 참고) https://jjangsungwon.tistory.com/30

![](https://images.velog.io/images/jsh5408/post/ffb9177d-b0b9-419b-938d-b9363164612e/image.png)
