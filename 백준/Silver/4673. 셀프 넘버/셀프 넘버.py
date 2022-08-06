nb = set(range(1, 10000))
r = set()
for num in nb :
    for n in str(num):
        num += int(n)
    r.add(num)
s_nb = nb - r
for s_n in sorted(s_nb): 
    print(s_n)