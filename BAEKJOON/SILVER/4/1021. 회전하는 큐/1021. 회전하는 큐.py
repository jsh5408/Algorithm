from collections import deque

n,m=map(int,input().split())
lst=deque(range(1,n+1))
q=deque(map(int,input().split()))

count=0
while q:
    mid=len(lst)//2
    if lst.index(q[0])>mid:
        while q[0]!=lst[0]:
            lst.appendleft(lst.pop())
            count+=1
        lst.popleft()
        q.popleft()
    else:
        while q[0]!=lst[0]:
            lst.append(lst.popleft())
            count+=1
        lst.popleft()
        q.popleft()
print(count)