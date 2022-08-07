fb = [0, 1]
for i in range(2, 50):
    fb.append(fb[i-2] + fb[i-1])
T = int(input())
for j in range(T):
    n = int(input())
    array = []
    while(n):
        for k in range(50):
            if (fb[k] <= n):
                t = fb[k]
        n-=t
        array.append(t)
        array.sort()
    for l in array:
        print(l, end=' ')