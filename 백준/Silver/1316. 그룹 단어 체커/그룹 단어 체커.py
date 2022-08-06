n = int(input())
group = 0
for _ in range(n):
    w = input()
    e = 0
    for index in range(len(w)-1): 
        if w[index] != w[index+1]:
            nw = w[index+1:]
            if nw.count(w[index]) > 0:
                e += 1 
    if e == 0:  
        group += 1
print(group)