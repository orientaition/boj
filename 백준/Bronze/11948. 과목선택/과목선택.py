import sys
input = sys.stdin.readline

sum=0
a=[]
for _ in range(4):
    a.append(int(input()))

a.sort()

for i in range(1,4):
    sum += a[i]

b = []
for _ in range(2):
    b.append(int(input()))

b.sort()
sum += b[1]
print(sum)
