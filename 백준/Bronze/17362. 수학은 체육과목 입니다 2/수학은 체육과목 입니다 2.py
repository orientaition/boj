import sys
input = sys.stdin.readline

a = int(input())
ans = a%8

if ans == 1 : print(1)
elif ans == 2 or ans == 0 : print(2)
elif ans == 3 or ans == 7 : print(3)
elif ans == 4 or ans == 6 : print(4)
else : print(5)

