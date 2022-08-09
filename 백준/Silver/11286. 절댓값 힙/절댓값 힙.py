import sys
import heapq
number = int(input())
hib = []
for _ in range(number):
    a = int(sys.stdin.readline())
    if a!=0:
        heapq.heappush(hib,(abs(a),a))
    else:
        if not hib:
            print(0)
        else:
            print(heapq.heappop(hib)[1])