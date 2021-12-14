from sys import stdin

N = int(stdin.readline())
people = []
rank = [1] * N

for i in range(N):
    x, y = map(int, stdin.readline().split())
    people.append((x, y))

for i in range(N):
    for j in range(i+1, N):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            rank[j] += 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

for r in rank:
    print(r, end=" ")