from sys import stdin
import collections

N = int(stdin.readline())

deque = collections.deque()

for _ in range(N):
    cmd = stdin.readline().split()
    
    if cmd[0] == "push_front":
        deque.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        deque.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif cmd[0] == "pop_back":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(deque))
    elif cmd[0] == "empty":
        if deque:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if deque:
            print(deque[-1])
        else:
            print(-1)