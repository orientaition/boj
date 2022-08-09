n = int(input())
m_r = []
for i in range(n):
    a,b = map(int,input().split())
    m_r.append([a,b])
m_r.sort(key=lambda x:x[0])
m_r.sort(key=lambda x:x[1])
cnt = 1
end = m_r[0][1]
for i in range(1,n):
    if m_r[i][0] >= end:
        cnt+=1
        end = m_r[i][1]
print(cnt)