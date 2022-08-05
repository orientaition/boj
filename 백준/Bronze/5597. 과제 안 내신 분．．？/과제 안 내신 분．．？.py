a = [i for i in range(1,31)]
for _ in range(28):
    a.remove(int(input()))
print(*a,sep="\n")