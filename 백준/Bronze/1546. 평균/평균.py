n = int(input())
t_l = list(map(int,input().split()))
MAX = max(t_l)
New = []
for score in t_l:
    New.append(score/MAX *100)
test = sum(New)/n
print(test)