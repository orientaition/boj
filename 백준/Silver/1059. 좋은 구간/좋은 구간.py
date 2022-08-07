l = int(input())
l_li = sorted(list(map(int,input().split())))
n = int(input())
l_li.sort()
if n in l_li: 
    print(0)
else:
    cnt=0
    m_n=0
    for i in l_li:
        if i<n:
            m_n=i
        elif i>n:
            M_n=i
            break
    for i in range(m_n+1,M_n-1):
        for j in range(i+1,M_n):
            if i<=n and j>=n:
                cnt+=1
    print(cnt)