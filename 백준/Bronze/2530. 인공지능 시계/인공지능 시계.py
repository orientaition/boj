h,m,s = map(int,input().split())
time = int(input())
s += time
m += s//60
h += m//60
print(h%24,m%60,s%60)