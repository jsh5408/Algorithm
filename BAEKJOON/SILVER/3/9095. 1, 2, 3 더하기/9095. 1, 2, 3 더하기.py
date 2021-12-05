from sys import stdin

T = int(stdin.readline())
cases = set()

def func(n, t):
    if n == 0:
        cases.add(t)
    elif n < 0:
        return
    
    func(n-1, t+"1")
    func(n-2, t+"2")
    func(n-3, t+"3")

for _ in range(T):
    n = int(stdin.readline())
    cases = set()
    func(n, "")
    print(len(cases))