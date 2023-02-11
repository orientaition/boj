import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i < MAX and not array[i]:
                array[i] = array[v] + 1
                q.append(i)
MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))