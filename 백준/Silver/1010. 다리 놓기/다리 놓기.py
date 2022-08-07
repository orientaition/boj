import math
a = int(input())
s_li = []
r_li = []
for i in range(0,a):
    n,m = map(int,input().split())
    s_li.append(n)
    r_li.append(m)
for i in range(0,len(s_li)):
    print(math.comb(r_li[i],s_li[i]))