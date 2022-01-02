from sys import stdin

A, B = map(int, stdin.readline().split())

a = set()
b = set()

for i in range(1, A+1):
    if A % i == 0:
        a.add(i)
    
for i in range(1, B+1):
    if B % i == 0:
        b.add(i)

gcd = a & b

print(max(gcd))
print((A*B)//max(gcd))