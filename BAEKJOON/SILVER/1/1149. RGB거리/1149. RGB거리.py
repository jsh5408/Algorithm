from sys import stdin

N = int(stdin.readline())
costs = []

for i in range(N):
    R, G, B = map(int, stdin.readline().split())
    costs.append([R, G, B])

for i in range(1, N):
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
    costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + costs[i][2]

print(min(costs[N-1]))