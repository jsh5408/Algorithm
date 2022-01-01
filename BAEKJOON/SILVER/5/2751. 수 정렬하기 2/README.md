## 2751. 수 정렬하기 2 - python3
https://www.acmicpc.net/problem/2751

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())

nums = []
for i in range(N):
    n = int(stdin.readline())
    nums.append(n)

nums.sort()

for n in nums:
    print(n)
```
nums 에 모두 저장 후 sort 하기

파이썬 기본 sort 는 O(nlog(n))

기본 sort 외에는 퀵 정렬이나 merge sort 등을 사용할 듯

![](https://images.velog.io/images/jsh5408/post/961f44bc-971a-48ce-994a-6e1a5df7ba02/image.png)

#### 다른 사람의 풀이
```
from sys import stdin

def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0

    while i < len(left) and j <len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k+=1
    
    if i==len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j==len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array

N = int(stdin.readline())

nums = [0] * N
for i in range(N):
    n = int(stdin.readline())
    nums[i] = n

nums = merge_sort(nums)

for n in nums:
    print(n)
```
merge sort 이용
left, mid, right 로 구역을 나눠서 정렬

넘 느리다...

![](https://images.velog.io/images/jsh5408/post/6be3c999-ae52-4798-ba80-848a02be46fb/image.png)