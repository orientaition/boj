n = int(input())
buy = [list(map(int,input().split()))for _ in range(n)]
for i in range(1,n):
    buy[i][0] = min(buy[i-1][1],buy[i-1][2])+buy[i][0]
    buy[i][1] = min(buy[i-1][0],buy[i-1][2])+buy[i][1]
    buy[i][2] = min(buy[i-1][0],buy[i-1][1])+buy[i][2]
print(min(buy[n-1]))