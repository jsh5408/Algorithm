from sys import stdin

N, M = map(int, stdin.readline().split())
dic = {}

for i in range(N):
    address, password = map(str, stdin.readline().split())
    dic[address] = password

for i in range(M):
    address = stdin.readline().strip()
    print(dic[address])