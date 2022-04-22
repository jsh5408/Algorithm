from sys import stdin
import collections

string = stdin.readline().strip()
string = string.upper()
dic = collections.Counter(string)

m = 0
ans = ""
flag = 0
for k, v in dic.items():
    if v > m:
        m = v
        ans = k
        flag = 0
    elif v == m:
        flag = 1

if flag:
    print("?")
else:
    print(ans)