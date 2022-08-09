n = int(input())
def ha(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        ha(n-1,a,c,b) 
        print(a,c)
        ha(n-1,b,a,c)
sum = 2**n-1
print(sum)
ha(n,1,2,3)