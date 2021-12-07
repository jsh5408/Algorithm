from sys import stdin

N = int(stdin.readline())
member = []

for i in range(N):
    age, name = stdin.readline().split()
    member.append((i, int(age), name))

member.sort(key = lambda x : (x[1], x[0]))

for m in member:
    print(str(m[1]) + " " + m[2])