import sys
n,k = map(int,input().split())
res = 0;
while bin(n).count('1')>k:
    n+=1
    res+=1
print(res)